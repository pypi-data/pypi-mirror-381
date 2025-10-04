"""
Tests for the matching_strategies_example module.
"""

import pytest
from unittest.mock import patch, MagicMock

from goodgleif.examples.matching_strategies_example import matching_strategies_example, main


class TestMatchingStrategiesExample:
    """Test the matching strategies example function."""
    
    @patch('goodgleif.examples.matching_strategies_example.CompanyMatcher')
    def test_matching_strategies_example(self, mock_company_matcher):
        """Test matching strategies example with mocked CompanyMatcher."""
        # Setup mock
        mock_gg = MagicMock()
        mock_gg.match_canonical.return_value = [
            {'original_name': 'Apple Inc.', 'score': 95.5}
        ]
        mock_gg.match_brief.return_value = [
            {'original_name': 'Apple Inc.', 'score': 88.2}
        ]
        mock_gg.match_best.return_value = [
            {
                'original_name': 'Apple Inc.',
                'canonical_score': 95.5,
                'brief_score': 88.2
            }
        ]
        mock_company_matcher.return_value = mock_gg
        
        # Test the function
        with patch('builtins.print'):
            result = matching_strategies_example("Apple Inc")
        
        # Verify calls
        mock_gg.load_data.assert_called_once()
        mock_gg.match_canonical.assert_called_once_with("Apple Inc", limit=2)
        mock_gg.match_brief.assert_called_once_with("Apple Inc", limit=2)
        mock_gg.match_best.assert_called_once_with("Apple Inc", limit=2)
        
        # Verify result structure
        assert 'canonical' in result
        assert 'brief' in result
        assert 'best' in result
        assert len(result['canonical']) == 1
        assert len(result['brief']) == 1
        assert len(result['best']) == 1
    
    def test_matching_strategies_example_defaults(self):
        """Test matching strategies example with default parameters."""
        with patch('goodgleif.examples.matching_strategies_example.CompanyMatcher') as mock_company_matcher:
            mock_gg = MagicMock()
            mock_gg.match_canonical.return_value = []
            mock_gg.match_brief.return_value = []
            mock_gg.match_best.return_value = []
            mock_company_matcher.return_value = mock_gg
            
            with patch('builtins.print'):
                result = matching_strategies_example()
            
            mock_gg.match_canonical.assert_called_once_with("Apple Inc", limit=2)
            mock_gg.match_brief.assert_called_once_with("Apple Inc", limit=2)
            mock_gg.match_best.assert_called_once_with("Apple Inc", limit=2)
    
    def test_main_function(self):
        """Test the main function."""
        with patch('goodgleif.examples.matching_strategies_example.matching_strategies_example') as mock_example:
            mock_example.return_value = {'test': 'data'}
            
            result = main()
            
            mock_example.assert_called_once()
            assert result == {'test': 'data'}
    
    def test_function_has_docstring(self):
        """Test that the function has a docstring."""
        assert matching_strategies_example.__doc__ is not None
        assert "Example comparing different matching strategies" in matching_strategies_example.__doc__
