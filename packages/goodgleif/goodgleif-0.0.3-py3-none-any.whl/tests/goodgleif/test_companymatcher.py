"""Tests for CompanyMatcher class."""

import pytest
import pandas as pd
from pathlib import Path

from goodgleif.companymatcher import CompanyMatcher


def test_companymatcher_init_default():
    """Test CompanyMatcher initialization with default path."""
    gg = CompanyMatcher()
    # The parquet_path should be set to a valid path
    assert gg.parquet_path is not None
    assert isinstance(gg.parquet_path, Path)
    # Data is not loaded until load_data() is called
    assert gg.df is None
    assert gg.canonical_names is None


def test_companymatcher_init_custom_path():
    """Test CompanyMatcher initialization with custom path."""
    custom_path = Path("/custom/path.parquet")
    gg = CompanyMatcher(custom_path)
    assert gg.parquet_path == custom_path


def test_companymatcher_attributes():
    """Test that CompanyMatcher has expected attributes."""
    gg = CompanyMatcher()
    
    # Check that the class has expected attributes
    assert hasattr(gg, 'df')
    assert hasattr(gg, 'canonical_names')
    assert hasattr(gg, 'parquet_path')
    
    # Check that methods exist
    assert hasattr(gg, 'load_data')
    assert hasattr(gg, 'search')
    assert hasattr(gg, 'match_best')


def test_companymatcher_methods_exist():
    """Test that CompanyMatcher methods exist and are callable."""
    gg = CompanyMatcher()
    
    # Check that methods exist and are callable
    assert callable(gg.load_data)
    assert callable(gg.search)
    assert callable(gg.match_best)


def test_companymatcher_usage_pattern():
    """Test the proper usage pattern of CompanyMatcher."""
    gg = CompanyMatcher()
    
    # Initially, data should not be loaded
    assert gg.df is None
    assert gg.canonical_names is None
    
    # The class should have the expected interface
    assert hasattr(gg, 'load_data')
    assert hasattr(gg, 'search')
    assert hasattr(gg, 'match_best')
    
    # These methods should be callable (even if they might fail without data)
    assert callable(gg.load_data)
    assert callable(gg.search)
    assert callable(gg.match_best)
