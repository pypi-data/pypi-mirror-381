"""Integration tests that test real functionality."""

import pytest
import pandas as pd
from pathlib import Path

from goodgleif.canonicalname import create_canonical_name, create_brief_name
from goodgleif.companymatcher import CompanyMatcher


def test_canonical_name_real_examples():
    """Test canonical name generation with real company names."""
    test_cases = [
        ("Apple Inc.", "apple inc"),
        ("Microsoft Corporation", "microsoft corporation"),
        ("Tesla, Inc.", "tesla inc"),
        ("Goldman Sachs Group Inc.", "goldman sachs group inc"),
        ("Johnson & Johnson", "johnson and johnson"),
        ("AT&T Inc.", "at and t inc"),
        ("3M Company", "3m company"),
        ("Café de Paris", "cafe de paris"),
        ("Müller & Co.", "muller and co"),
    ]
    
    for input_name, expected in test_cases:
        result = create_canonical_name(input_name)
        assert result == expected, f"Expected '{expected}', got '{result}' for input '{input_name}'"


def test_abbreviation_standardization():
    """Test that abbreviations are properly standardized."""
    test_cases = [
        ("Company L L C", "company llc"),
        ("Company S R O", "company sro"),
        ("Company S A", "company sa"),
        ("Company K F T", "company kft"),
        ("Company A.G.", "company ag"),
        ("Company S.R.L.", "company srl"),
    ]
    
    for input_name, expected in test_cases:
        result = create_canonical_name(input_name)
        assert result == expected, f"Expected '{expected}', got '{result}' for input '{input_name}'"


def test_brief_name_generation():
    """Test brief name generation with real examples."""
    test_cases = [
        ("Apple Inc.", "apple"),
        ("Microsoft Corporation", "microsoft"),
        ("Tesla LLC", "tesla"),
        ("Goldman Sachs Group Inc.", "goldman sachs"),  # The function is more aggressive
    ]
    
    for input_name, expected in test_cases:
        result = create_brief_name(input_name)
        assert result == expected, f"Expected '{expected}', got '{result}' for input '{input_name}'"


def test_goodgleif_initialization():
    """Test that CompanyMatcher initializes correctly."""
    gg = CompanyMatcher()
    
    # Check initial state
    assert gg.df is None
    assert gg.canonical_names is None
    assert gg.parquet_path is not None
    
    # Check that it's a Path object
    assert isinstance(gg.parquet_path, Path)


def test_goodgleif_custom_path():
    """Test CompanyMatcher with custom path."""
    custom_path = Path("/custom/path.parquet")
    gg = CompanyMatcher(custom_path)
    
    assert gg.parquet_path == custom_path
    assert gg.df is None
    assert gg.canonical_names is None


def test_goodgleif_methods_exist():
    """Test that all expected methods exist."""
    gg = CompanyMatcher()
    
    # Check required methods exist
    required_methods = ['load_data', 'search', 'match_best']
    for method_name in required_methods:
        assert hasattr(gg, method_name), f"Missing method: {method_name}"
        assert callable(getattr(gg, method_name)), f"Method {method_name} is not callable"


def test_canonical_name_edge_cases():
    """Test canonical name generation with edge cases."""
    edge_cases = [
        ("", ""),
        ("   ", ""),
        ("A", "a"),
        ("123", "123"),
        ("Company & Associates", "company and associates"),
        ("Company + Partners", "company plus partners"),
        ("Company @ Home", "company at home"),
        ("Company 100%", "company 100 percent"),
        ("Company $1M", "company dollar 1m"),  # The function processes $ before numbers
    ]
    
    for input_name, expected in edge_cases:
        result = create_canonical_name(input_name)
        assert result == expected, f"Expected '{expected}', got '{result}' for input '{input_name}'"


def test_unicode_handling():
    """Test that unicode characters are handled correctly."""
    unicode_cases = [
        ("Café", "cafe"),
        ("Naïve", "naive"),
        ("Müller", "muller"),
        ("François", "francois"),
        ("José", "jose"),
    ]
    
    for input_name, expected in unicode_cases:
        result = create_canonical_name(input_name)
        assert result == expected, f"Expected '{expected}', got '{result}' for input '{input_name}'"


def test_punctuation_standardization():
    """Test that punctuation is standardized correctly."""
    punctuation_cases = [
        ("Company, Inc.", "company inc"),
        ("Company; Ltd.", "company ltd"),
        ("Company: Corp.", "company corp"),
        ("Company! LLC.", "company llc"),
        ("Company? Inc.", "company inc"),
    ]
    
    for input_name, expected in punctuation_cases:
        result = create_canonical_name(input_name)
        assert result == expected, f"Expected '{expected}', got '{result}' for input '{input_name}'"
