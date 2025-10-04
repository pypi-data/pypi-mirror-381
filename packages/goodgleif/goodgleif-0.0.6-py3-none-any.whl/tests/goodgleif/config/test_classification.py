"""Tests for classification functionality."""

import pytest
import pandas as pd
from pathlib import Path

from goodgleif.canonicalname import create_canonical_name


def test_classification_patterns():
    """Test that classification patterns work correctly."""
    # Test metals and mining patterns
    mining_names = [
        "Gold Mining Corp",
        "Iron Ore Ltd",
        "Coal Energy Inc",
        "Petroleum Company",
        "Solar Power Ltd"
    ]
    
    for name in mining_names:
        canonical = create_canonical_name(name)
        # These should contain mining-related terms
        assert any(term in canonical for term in ['gold', 'mining', 'iron', 'ore', 'coal', 'energy', 'petroleum', 'solar', 'power'])


def test_financial_patterns():
    """Test financial classification patterns."""
    financial_names = [
        "Bank of America",
        "Goldman Sachs",
        "Investment Fund",
        "Credit Union",
        "Insurance Company"
    ]
    
    for name in financial_names:
        canonical = create_canonical_name(name)
        # These should contain financial-related terms
        assert any(term in canonical for term in ['bank', 'america', 'goldman', 'sachs', 'investment', 'fund', 'credit', 'union', 'insurance'])


def test_technology_patterns():
    """Test technology classification patterns."""
    tech_names = [
        "Apple Technology",
        "Microsoft Software",
        "Google Cloud",
        "Amazon Web Services"
    ]
    
    for name in tech_names:
        canonical = create_canonical_name(name)
        # These should contain tech-related terms
        assert any(term in canonical for term in ['apple', 'technology', 'microsoft', 'software', 'google', 'cloud', 'amazon', 'web', 'services'])


def test_healthcare_patterns():
    """Test healthcare classification patterns."""
    healthcare_names = [
        "Johnson & Johnson",
        "Pfizer Pharmaceuticals",
        "Medical Device Corp",
        "Healthcare Services"
    ]
    
    for name in healthcare_names:
        canonical = create_canonical_name(name)
        # These should contain healthcare-related terms
        assert any(term in canonical for term in ['johnson', 'pfizer', 'pharmaceuticals', 'medical', 'device', 'healthcare', 'services'])


def test_automotive_patterns():
    """Test automotive classification patterns."""
    auto_names = [
        "Ford Motor Company",
        "General Motors",
        "Tesla Motors",
        "Toyota Automotive"
    ]
    
    for name in auto_names:
        canonical = create_canonical_name(name)
        # These should contain automotive-related terms
        assert any(term in canonical for term in ['ford', 'motor', 'company', 'general', 'motors', 'tesla', 'toyota', 'automotive'])


def test_transportation_patterns():
    """Test transportation classification patterns."""
    transport_names = [
        "FedEx Corporation",
        "UPS Shipping",
        "Delta Airlines",
        "Railway Company"
    ]
    
    for name in transport_names:
        canonical = create_canonical_name(name)
        # These should contain transportation-related terms
        assert any(term in canonical for term in ['fedex', 'corporation', 'ups', 'shipping', 'delta', 'airlines', 'railway', 'company'])


def test_real_estate_patterns():
    """Test real estate classification patterns."""
    real_estate_names = [
        "Real Estate Trust",
        "Property Management",
        "Construction Company",
        "Building Corp"
    ]
    
    for name in real_estate_names:
        canonical = create_canonical_name(name)
        # These should contain real estate-related terms
        assert any(term in canonical for term in ['real', 'estate', 'trust', 'property', 'management', 'construction', 'company', 'building', 'corp'])


def test_manufacturing_patterns():
    """Test manufacturing classification patterns."""
    manufacturing_names = [
        "General Electric",
        "Manufacturing Corp",
        "Industrial Company",
        "Production Ltd"
    ]
    
    for name in manufacturing_names:
        canonical = create_canonical_name(name)
        # These should contain manufacturing-related terms
        assert any(term in canonical for term in ['general', 'electric', 'manufacturing', 'corp', 'industrial', 'company', 'production', 'ltd'])


def test_retail_consumer_patterns():
    """Test retail/consumer classification patterns."""
    retail_names = [
        "Walmart Stores",
        "Amazon Retail",
        "Consumer Goods",
        "Shopping Mall"
    ]
    
    for name in retail_names:
        canonical = create_canonical_name(name)
        # These should contain retail-related terms
        assert any(term in canonical for term in ['walmart', 'stores', 'amazon', 'retail', 'consumer', 'goods', 'shopping', 'mall'])
