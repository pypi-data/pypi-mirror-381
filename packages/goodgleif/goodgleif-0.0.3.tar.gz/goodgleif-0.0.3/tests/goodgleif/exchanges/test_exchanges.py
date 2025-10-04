"""Tests for exchange data loading functionality."""

import pytest
import pandas as pd

from goodgleif.exchanges import ASXLoader, LSELoader, TSXLoader


def test_sample_data_functions():
    """Test sample data functions return expected format."""
    # Test ASX sample
    asx_loader = ASXLoader()
    asx_df = asx_loader.get_sample_data()
    assert len(asx_df) > 0
    assert 'ticker' in asx_df.columns
    assert 'name' in asx_df.columns
    assert 'country' in asx_df.columns
    assert 'exchange' in asx_df.columns
    assert asx_df['country'].iloc[0] == 'AU'
    assert asx_df['exchange'].iloc[0] == 'ASX'
    
    # Test LSE sample
    lse_loader = LSELoader()
    lse_df = lse_loader.get_sample_data()
    assert len(lse_df) > 0
    assert lse_df['country'].iloc[0] == 'GB'
    assert lse_df['exchange'].iloc[0] == 'LSE'
    
    # Test TSX sample
    tsx_loader = TSXLoader()
    tsx_df = tsx_loader.get_sample_data()
    assert len(tsx_df) > 0
    assert tsx_df['country'].iloc[0] == 'CA'
    assert tsx_df['exchange'].iloc[0] == 'TSX'


def test_sample_data_content():
    """Test that sample data contains expected companies."""
    # Test ASX sample contains mining companies
    asx_loader = ASXLoader()
    asx_df = asx_loader.get_sample_data()
    mining_companies = asx_df[asx_df['industry'] == 'Materials']
    assert len(mining_companies) >= 4  # BHP, RIO, FMG, NCM
    
    # Test LSE sample contains mining companies
    lse_loader = LSELoader()
    lse_df = lse_loader.get_sample_data()
    assert 'Anglo American' in lse_df['name'].iloc[0]
    assert 'Glencore' in lse_df['name'].iloc[1]
    
    # Test TSX sample contains mining companies
    tsx_loader = TSXLoader()
    tsx_df = tsx_loader.get_sample_data()
    assert 'Barrick Gold' in tsx_df['name'].iloc[0]
    assert 'Franco-Nevada' in tsx_df['name'].iloc[1]


def test_exchange_data_structure():
    """Test that exchange data has the expected structure."""
    # Test ASX structure
    asx_loader = ASXLoader()
    asx_df = asx_loader.get_sample_data()
    expected_cols = ['ticker', 'name', 'country', 'exchange']
    for col in expected_cols:
        assert col in asx_df.columns
    
    # Test LSE structure
    lse_loader = LSELoader()
    lse_df = lse_loader.get_sample_data()
    for col in expected_cols:
        assert col in lse_df.columns
    
    # Test TSX structure
    tsx_loader = TSXLoader()
    tsx_df = tsx_loader.get_sample_data()
    for col in expected_cols:
        assert col in tsx_df.columns


def test_exchange_data_types():
    """Test that exchange data has correct data types."""
    asx_loader = ASXLoader()
    asx_df = asx_loader.get_sample_data()
    
    # Check data types
    assert asx_df['ticker'].dtype == 'object'
    assert asx_df['name'].dtype == 'object'
    assert asx_df['country'].dtype == 'object'
    assert asx_df['exchange'].dtype == 'object'
    
    # Check that no essential fields are empty
    assert not asx_df['ticker'].isna().any()
    assert not asx_df['name'].isna().any()
    assert not asx_df['country'].isna().any()
    assert not asx_df['exchange'].isna().any()


def test_exchange_data_consistency():
    """Test that exchange data is consistent."""
    asx_loader = ASXLoader()
    asx_df = asx_loader.get_sample_data()
    lse_loader = LSELoader()
    lse_df = lse_loader.get_sample_data()
    tsx_loader = TSXLoader()
    tsx_df = tsx_loader.get_sample_data()
    
    # All ASX companies should have country 'AU'
    assert (asx_df['country'] == 'AU').all()
    assert (asx_df['exchange'] == 'ASX').all()
    
    # All LSE companies should have country 'GB'
    assert (lse_df['country'] == 'GB').all()
    assert (lse_df['exchange'] == 'LSE').all()
    
    # All TSX companies should have country 'CA'
    assert (tsx_df['country'] == 'CA').all()
    assert (tsx_df['exchange'] == 'TSX').all()


def test_exchange_loaders_exist():
    """Test that exchange loaders exist and are callable."""
    # Test that loaders exist
    assert callable(ASXLoader)
    assert callable(LSELoader)
    assert callable(TSXLoader)


def test_exchange_functions_return_dataframes():
    """Test that exchange functions return pandas DataFrames."""
    asx_loader = ASXLoader()
    asx_df = asx_loader.get_sample_data()
    lse_loader = LSELoader()
    lse_df = lse_loader.get_sample_data()
    tsx_loader = TSXLoader()
    tsx_df = tsx_loader.get_sample_data()
    
    assert isinstance(asx_df, pd.DataFrame)
    assert isinstance(lse_df, pd.DataFrame)
    assert isinstance(tsx_df, pd.DataFrame)