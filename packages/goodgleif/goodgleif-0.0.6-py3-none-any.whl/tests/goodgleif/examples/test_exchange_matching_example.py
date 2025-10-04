"""
Tests for the exchange_matching_example module.
"""

import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

from goodgleif.examples.exchange_matching_example import (
    exchange_matching_example, 
    main,
    _match_exchange_companies,
    _get_sample_exchange_data,
    _sample_asx_data,
    _sample_lse_data,
    _sample_tsx_data
)


class TestExchangeMatchingExample:
    """Test the exchange matching example function."""
    
    @patch('goodgleif.examples.exchange_matching_example.CompanyMatcher')
    def test_exchange_matching_example(self, mock_company_matcher):
        """Test exchange matching example with mocked CompanyMatcher."""
        # Setup mock
        mock_gg = MagicMock()
        mock_gg.df = pd.DataFrame({'lei': ['LEI1', 'LEI2'], 'name': ['Company1', 'Company2']})
        mock_gg.match_best.return_value = [
            {
                'original_name': 'BHP Group Limited',
                'score': 95.5,
                'lei': 'HWUPKR0MPOU8FGXBT394',
                'country': 'AU'
            }
        ]
        mock_company_matcher.return_value = mock_gg
        
        # Create sample exchange data
        sample_data = {
            'ASX': pd.DataFrame([
                {'ticker': 'BHP', 'name': 'BHP Group Limited', 'country': 'AU', 'exchange': 'ASX', 'industry': 'Materials'}
            ])
        }
        
        # Test the function
        with patch('builtins.print'):
            result = exchange_matching_example(sample_data, min_score=80)
        
        # Verify calls
        mock_gg.load_data.assert_called_once()
        mock_gg.match_best.assert_called_once_with('BHP Group Limited', limit=1, min_score=80)
        
        # Verify result structure
        assert 'ASX' in result
        assert 'matches' in result['ASX']
        assert 'no_matches' in result['ASX']
        assert 'total' in result['ASX']
        assert 'match_rate' in result['ASX']
        assert result['ASX']['total'] == 1
        assert len(result['ASX']['matches']) == 1
        assert result['ASX']['match_rate'] == 100.0
    
    def test_exchange_matching_example_defaults(self):
        """Test exchange matching example with default parameters."""
        with patch('goodgleif.examples.exchange_matching_example.CompanyMatcher') as mock_company_matcher:
            mock_gg = MagicMock()
            mock_gg.df = pd.DataFrame({'lei': ['LEI1'], 'name': ['Company1']})
            mock_gg.match_best.return_value = []
            mock_company_matcher.return_value = mock_gg
            
            with patch('builtins.print'):
                result = exchange_matching_example()
            
            # Should use sample data by default
            assert 'ASX' in result
            assert 'LSE' in result
            assert 'TSX' in result
    
    def test_main_function(self):
        """Test the main function."""
        with patch('goodgleif.examples.exchange_matching_example.exchange_matching_example') as mock_example:
            mock_example.return_value = {'test': 'data'}
            
            result = main()
            
            mock_example.assert_called_once()
            assert result == {'test': 'data'}
    
    def test_function_has_docstring(self):
        """Test that the function has a docstring."""
        assert exchange_matching_example.__doc__ is not None
        assert "Example: Match companies from various stock exchanges" in exchange_matching_example.__doc__


class TestHelperFunctions:
    """Test the helper functions in the exchange matching example."""
    
    def test_match_exchange_companies(self):
        """Test the _match_exchange_companies helper function."""
        # Create test data
        companies_df = pd.DataFrame([
            {'ticker': 'BHP', 'name': 'BHP Group Limited', 'industry': 'Materials'}
        ])
        
        # Mock CompanyMatcher
        mock_gg = MagicMock()
        mock_gg.match_best.return_value = [
            {
                'original_name': 'BHP Group Limited',
                'score': 95.5,
                'lei': 'HWUPKR0MPOU8FGXBT394',
                'country': 'AU'
            }
        ]
        
        with patch('builtins.print'):
            result = _match_exchange_companies('ASX', companies_df, mock_gg, min_score=80)
        
        # Verify result structure
        assert result['total'] == 1
        assert len(result['matches']) == 1
        assert len(result['no_matches']) == 0
        assert result['match_rate'] == 100.0
        
        # Verify match data
        match = result['matches'][0]
        assert match['exchange'] == 'ASX'
        assert match['ticker'] == 'BHP'
        assert match['exchange_name'] == 'BHP Group Limited'
        assert match['gleif_name'] == 'BHP Group Limited'
        assert match['score'] == 95.5
    
    def test_get_sample_exchange_data(self):
        """Test the _get_sample_exchange_data helper function."""
        result = _get_sample_exchange_data()
        
        assert 'ASX' in result
        assert 'LSE' in result
        assert 'TSX' in result
        
        # Verify data structure
        for exchange, df in result.items():
            assert isinstance(df, pd.DataFrame)
            assert 'ticker' in df.columns
            assert 'name' in df.columns
            assert 'country' in df.columns
            assert 'exchange' in df.columns
            assert 'industry' in df.columns
    
    def test_sample_data_functions(self):
        """Test the individual sample data functions."""
        # Test ASX data
        asx_data = _sample_asx_data()
        assert isinstance(asx_data, pd.DataFrame)
        assert len(asx_data) == 5
        assert all(asx_data['exchange'] == 'ASX')
        
        # Test LSE data
        lse_data = _sample_lse_data()
        assert isinstance(lse_data, pd.DataFrame)
        assert len(lse_data) == 5
        assert all(lse_data['exchange'] == 'LSE')
        
        # Test TSX data
        tsx_data = _sample_tsx_data()
        assert isinstance(tsx_data, pd.DataFrame)
        assert len(tsx_data) == 5
        assert all(tsx_data['exchange'] == 'TSX')
