# GoodGleif

A Python package for generating canonical company names and fuzzy matching against the GLEIF database.

## Core Purpose

**Canonical Name Generation**: Standardize company names for consistent matching by:
- Converting to lowercase and normalizing Unicode
- Removing extra whitespace and standardizing punctuation  
- Applying abbreviation standardizations (LLC, SRO, AS, etc.)
- Creating brief names for better matching

## Features

- **Fuzzy Company Matching**: Match company names against the GLEIF database
- **Exchange Data Loading**: Load company lists from major stock exchanges (ASX, LSE, TSX)
- **Classification System**: Binary flags for company categorization
- **Partitioned Data**: GitHub-friendly data distribution with automatic loading

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from goodgleif import create_canonical_name, GoodGleif

# Generate canonical company names
canonical = create_canonical_name("Apple Inc.")
print(canonical)  # "apple inc"

# Match against GLEIF database
gg = GoodGleif()
gg.load_data()
matches = gg.search("Apple Inc", limit=5)
print(matches)
```

## Exchange Data

Load company lists from major stock exchanges:

```python
from goodgleif import load_asx, load_lse, load_tsx

# Load ASX companies
asx_companies = load_asx()

# Load LSE companies  
lse_companies = load_lse()

# Load TSX companies
tsx_companies = load_tsx()
```

## Scripts

See the `scripts/` directory for utility scripts:

- `filter_gleif.py` - Main dataset builder with classification flags
- `explore_dataset.py` - Dataset exploration and analysis
- `query_demo.py` - Query demonstration and testing

## Data Structure

The package works with classified GLEIF data that includes:

- **LEI**: Legal Entity Identifier
- **LegalName**: Company legal name
- **Country**: Company country
- **Category/SubCategory**: GLEIF entity categories
- **Classification Flags**: Binary flags for company types (mining, financial, etc.)

## Development

Run tests:
```bash
python -m pytest tests/ -v
```

Build the classified dataset:
```bash
python scripts/filter_gleif.py
```

## License

See LICENSE file for details.