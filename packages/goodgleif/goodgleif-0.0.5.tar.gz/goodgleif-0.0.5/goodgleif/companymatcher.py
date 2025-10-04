"""
GoodGleif class for fuzzy company name matching against GLEIF data.
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import List, Optional, Tuple

import pandas as pd
from rapidfuzz import fuzz, process

from .canonicalname import create_canonical_name, create_brief_name


class CompanyMatcher:
    """
    Fuzzy company name matching against GLEIF real companies data.
    """
    
    def __init__(self, parquet_path: Optional[Path] = None):
        """
        Initialize with path to gleif_classified data.
        
        Args:
            parquet_path: Path to the classified parquet file. If None, uses default.
        """
        if parquet_path is None:
            # Default to classified data with partitioned files
            from goodgleif.whereami import get_project_root
            parquet_path = get_project_root() / "data_local" / "gleif_classified.parquet"
        
        self.parquet_path = Path(parquet_path)
        self.df: Optional[pd.DataFrame] = None
        self.canonical_names: Optional[List[str]] = None
        
    def load_data(self) -> None:
        """Load the parquet data and canonical names."""
        base_path = self.parquet_path.parent
        manifest_path = base_path / "gleif_classified_manifest.txt"
        
        # Check for partitioned files in data_local first
        if manifest_path.exists():
            print(f"Loading partitioned GLEIF data from: {base_path}")
            self._load_partitioned_data(base_path)
        # Check for package-distributed partitioned files
        elif self._load_package_partitioned_data():
            print("Loading partitioned GLEIF data from package...")
        elif self.parquet_path.exists():
            print(f"Loading GLEIF data from: {self.parquet_path}")
            self.df = pd.read_parquet(self.parquet_path)
        else:
            raise FileNotFoundError(f"GLEIF data not found. Please run 'python debug/filter_gleif.py' to generate the classified dataset.")
        
        # Use pre-computed canonical names if available, otherwise create them
        if 'canonical_name' in self.df.columns:
            print("Using pre-computed canonical names...")
            self.canonical_names = self.df['canonical_name'].tolist()
        else:
            print("Creating canonical names for fuzzy matching...")
            self.canonical_names = [
                create_canonical_name(name) 
                for name in self.df['Entity.LegalName']
            ]
        
        print(f"Loaded {len(self.df):,} companies")
    
    def _load_partitioned_data(self, base_path: Path) -> None:
        """Load data from partitioned files."""
        partitions = []
        
        # Load all partition files
        for i in range(1, 6):  # Parts 1-5
            partition_path = base_path / f"gleif_classified_part_{i}.parquet"
            if partition_path.exists():
                print(f"  Loading partition {i}...")
                partition_df = pd.read_parquet(partition_path)
                partitions.append(partition_df)
            else:
                print(f"  Warning: Partition {i} not found: {partition_path}")
        
        if not partitions:
            raise FileNotFoundError("No partition files found")
        
        # Combine all partitions
        print(f"  Combining {len(partitions)} partitions...")
        self.df = pd.concat(partitions, ignore_index=True)
        print(f"  Combined dataset: {len(self.df):,} companies")
    
    def _load_package_partitioned_data(self) -> bool:
        """Load data from package-distributed partitioned files."""
        try:
            from goodgleif.paths import open_resource_path
            
            partitions = []
            
            # Try to load all partition files from package resources
            for i in range(1, 6):  # Parts 1-5
                try:
                    with open_resource_path(f"gleif_classified_part_{i}.parquet") as partition_path:
                        print(f"  Loading partition {i} from package...")
                        partition_df = pd.read_parquet(partition_path)
                        partitions.append(partition_df)
                except FileNotFoundError:
                    # If any partition is missing, return False
                    return False
            
            if partitions:
                # Combine all partitions
                print(f"  Combining {len(partitions)} partitions...")
                self.df = pd.concat(partitions, ignore_index=True)
                print(f"  Combined dataset: {len(self.df):,} companies")
                return True
            
            return False
            
        except ImportError:
            # Package resources not available
            return False
    
    def search(self, query: str, limit: int = 10, min_score: int = 60) -> pd.DataFrame:
        """
        Search for companies matching the query using fuzzy matching.
        
        Args:
            query: Company name to search for
            limit: Maximum number of results to return
            min_score: Minimum fuzzy match score (0-100)
            
        Returns:
            DataFrame with matching companies and their scores
        """
        if self.df is None or self.canonical_names is None:
            self.load_data()
        
        # Create canonical version of query
        canonical_query = create_canonical_name(query)
        
        if not canonical_query:
            return pd.DataFrame()
        
        # Use rapidfuzz for fast fuzzy matching
        matches = process.extract(
            canonical_query,
            self.canonical_names,
            scorer=fuzz.ratio,
            limit=limit * 2  # Get more than needed to filter by score
        )
        
        # Filter by minimum score and get indices
        results = []
        for match_text, score, idx in matches:
            if score >= min_score:
                results.append({
                    'original_name': self.df.iloc[idx]['Entity.LegalName'],
                    'canonical_name': match_text,
                    'score': score,
                    'lei': self.df.iloc[idx]['LEI'],
                    'category': self.df.iloc[idx].get('Entity.EntityCategory', 'N/A'),
                    'subcategory': self.df.iloc[idx].get('Entity.EntitySubCategory', 'N/A'),
                    'country': self.df.iloc[idx].get('Entity.LegalAddress.Country', 'N/A'),
                    'real_flag': self.df.iloc[idx].get('REAL_FLAG', 0)
                })
        
        # Convert to DataFrame and sort by score
        results_df = pd.DataFrame(results)
        if not results_df.empty:
            results_df = results_df.sort_values('score', ascending=False).head(limit)
        
        return results_df
    
    def get_shortlist(self, query: str, limit: int = 10, min_score: int = 70) -> List[dict]:
        """
        Get a shortlist of the best matches for a company name.
        
        Args:
            query: Company name to search for
            limit: Maximum number of results to return
            min_score: Minimum fuzzy match score (0-100)
            
        Returns:
            List of dictionaries with match information
        """
        results_df = self.search(query, limit, min_score)
        
        if results_df.empty:
            return []
        
        return results_df.to_dict('records')
    
    def get_canonical_name(self, company_name: str) -> str:
        """
        Create a canonical name for a given company name.
        
        Args:
            company_name: Company name to standardize
            
        Returns:
            Canonical version of the company name
        """
        return create_canonical_name(company_name)
    
    def get_brief_name(self, company_name: str) -> str:
        """
        Create a brief name for a given company name (removes legal suffixes).
        
        Args:
            company_name: Company name to standardize
            
        Returns:
            Brief version of the company name
        """
        return create_brief_name(company_name)
    
    def match_canonical(self, query: str, limit: int = 10, min_score: int = 70, country: Optional[str] = None) -> List[dict]:
        """
        Match against canonical names (preserves legal suffixes).
        
        Args:
            query: Company name to search for
            limit: Maximum number of results
            min_score: Minimum fuzzy match score
            country: Optional country code to filter by (matches any .Country column)
            
        Returns:
            List of matching companies
        """
        if self.df is None or self.canonical_names is None:
            self.load_data()
        
        canonical_query = create_canonical_name(query)
        return self._perform_search(canonical_query, self.canonical_names, limit, min_score, country)
    
    def match_brief(self, query: str, limit: int = 10, min_score: int = 70, country: Optional[str] = None) -> List[dict]:
        """
        Match against brief names (removes legal suffixes).
        
        Args:
            query: Company name to search for
            limit: Maximum number of results
            min_score: Minimum fuzzy match score
            country: Optional country code to filter by (matches any .Country column)
            
        Returns:
            List of matching companies
        """
        if self.df is None or self.canonical_names is None:
            self.load_data()
        
        # Create brief names if not already available
        if 'brief_name' not in self.df.columns:
            self.df['brief_name'] = self.df['Entity.LegalName'].apply(create_brief_name)
        
        brief_names = self.df['brief_name'].tolist()
        brief_query = create_brief_name(query)
        return self._perform_search(brief_query, brief_names, limit, min_score, country)
    
    def match_best(self, query: str, limit: int = 10, min_score: int = 70, country: Optional[str] = None) -> List[dict]:
        """
        Get the best matches using both canonical and brief name matching.
        
        Args:
            query: Company name to search for
            limit: Maximum number of results
            min_score: Minimum fuzzy match score
            country: Optional country code to filter by (matches any .Country column)
            
        Returns:
            List of matching companies with both canonical and brief scores
        """
        if self.df is None or self.canonical_names is None:
            self.load_data()
        
        canonical_query = create_canonical_name(query)
        brief_query = create_brief_name(query)
        
        # Create brief names if not already available
        if 'brief_name' not in self.df.columns:
            self.df['brief_name'] = self.df['Entity.LegalName'].apply(create_brief_name)
        
        brief_names = self.df['brief_name'].tolist()
        
        # Get matches from both approaches
        canonical_matches = self._perform_search(canonical_query, self.canonical_names, limit * 2, min_score, country)
        brief_matches = self._perform_search(brief_query, brief_names, limit * 2, min_score, country)
        
        # Combine and deduplicate by LEI
        all_matches = {}
        
        for match in canonical_matches:
            lei = match['lei']
            if lei not in all_matches:
                all_matches[lei] = match
                all_matches[lei]['canonical_score'] = match['score']
                all_matches[lei]['brief_score'] = 0
            else:
                all_matches[lei]['canonical_score'] = match['score']
        
        for match in brief_matches:
            lei = match['lei']
            if lei not in all_matches:
                all_matches[lei] = match
                all_matches[lei]['canonical_score'] = 0
                all_matches[lei]['brief_score'] = match['score']
            else:
                all_matches[lei]['brief_score'] = match['score']
        
        # Calculate combined score and sort
        for lei, match in all_matches.items():
            canonical_score = match.get('canonical_score', 0)
            brief_score = match.get('brief_score', 0)
            match['combined_score'] = max(canonical_score, brief_score)  # Use the higher score
        
        # Sort by combined score and return top results
        sorted_matches = sorted(all_matches.values(), key=lambda x: x['combined_score'], reverse=True)
        return sorted_matches[:limit]
    
    def _perform_search(self, query: str, name_list: List[str], limit: int, min_score: int, country: Optional[str] = None) -> List[dict]:
        """Internal method to perform fuzzy search with optional country filtering."""
        if not query:
            return []
        
        matches = process.extract(
            query,
            name_list,
            scorer=fuzz.ratio,
            limit=limit * 2
        )
        
        results = []
        for match_text, score, idx in matches:
            if score >= min_score:
                # Check country filter if provided
                if country:
                    country_match = self._check_country_match(self.df.iloc[idx], country)
                    if not country_match:
                        continue
                
                results.append({
                    'original_name': self.df.iloc[idx]['Entity.LegalName'],
                    'canonical_name': self.df.iloc[idx].get('canonical_name', ''),
                    'brief_name': self.df.iloc[idx].get('brief_name', ''),
                    'score': score,
                    'lei': self.df.iloc[idx]['LEI'],
                    'category': self.df.iloc[idx].get('Entity.EntityCategory', 'N/A'),
                    'subcategory': self.df.iloc[idx].get('Entity.EntitySubCategory', 'N/A'),
                    'country': self.df.iloc[idx].get('Entity.LegalAddress.Country', 'N/A'),
                    'real_flag': self.df.iloc[idx].get('REAL_FLAG', 0)
                })
        
        return sorted(results, key=lambda x: x['score'], reverse=True)[:limit]
    
    def _check_country_match(self, row: pd.Series, country: str) -> bool:
        """
        Check if a row matches the country filter by looking at any column ending in .Country.
        
        Args:
            row: DataFrame row to check
            country: Country code to match (case-insensitive)
            
        Returns:
            True if any .Country column matches the country code
        """
        if not country:
            return True
        
        country_upper = country.upper()
        
        # Find all columns ending in .Country
        country_columns = [col for col in row.index if col.endswith('.Country')]
        
        for col in country_columns:
            value = row.get(col, '')
            if pd.notna(value) and str(value).upper() == country_upper:
                return True
        
        return False
    
    def get_stats(self) -> dict:
        """Get statistics about the loaded dataset."""
        if self.df is None:
            return {}
        
        stats = {
            'total_companies': len(self.df),
            'real_businesses': int(self.df['REAL_FLAG'].sum()) if 'REAL_FLAG' in self.df.columns else 0,
            'non_financial_entities': len(self.df) - int(self.df['REAL_FLAG'].sum()) if 'REAL_FLAG' in self.df.columns else len(self.df),
            'countries': self.df['Entity.LegalAddress.Country'].nunique() if 'Entity.LegalAddress.Country' in self.df.columns else 0,
            'categories': self.df['Entity.EntityCategory'].nunique() if 'Entity.EntityCategory' in self.df.columns else 0,
        }
        
        return stats
