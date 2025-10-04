"""
Tests for the simple_usage_example module.
"""

import pytest
from unittest.mock import patch, MagicMock

from goodgleif.examples.simple_usage_example import simple_usage_example, main


class TestSimpleUsageExample:
    """Test the simple usage example function."""
    
    @patch('goodgleif.examples.simple_usage_example.CompanyMatcher')
    def test_simple_usage_example(self, mock_company_matcher):
        """Test simple usage example with mocked CompanyMatcher."""
        # Setup mock
        mock_gg = MagicMock()
        mock_gg.match_best.side_effect = [
            [{'original_name': 'Apple Inc.', 'score': 95.5, 'lei': 'HWUPKR0MPOU8FGXBT394', 'country': 'US'}],
            [{'original_name': 'Microsoft Corporation', 'score': 92.3, 'lei': 'HWUPKR0MPOU8FGXBT395', 'country': 'US'}],
            [{'original_name': 'Tesla Inc.', 'score': 88.7, 'lei': 'HWUPKR0MPOU8FGXBT396', 'country': 'US'}],
            [{'original_name': 'Goldman Sachs Group Inc.', 'score': 85.1, 'lei': 'HWUPKR0MPOU8FGXBT397', 'country': 'US'}]
        ]
        mock_company_matcher.return_value = mock_gg
        
        # Test the function
        with patch('builtins.print'):
            result = simple_usage_example(["Apple", "Microsoft", "Tesla", "Goldman Sachs"])
        
        # Verify calls
        assert mock_gg.match_best.call_count == 4
        mock_gg.match_best.assert_any_call("Apple", limit=3, min_score=80)
        mock_gg.match_best.assert_any_call("Microsoft", limit=3, min_score=80)
        mock_gg.match_best.assert_any_call("Tesla", limit=3, min_score=80)
        mock_gg.match_best.assert_any_call("Goldman Sachs", limit=3, min_score=80)
        
        # Verify result structure
        assert 'Apple' in result
        assert 'Microsoft' in result
        assert 'Tesla' in result
        assert 'Goldman Sachs' in result
        assert len(result['Apple']) == 1
        assert result['Apple'][0]['original_name'] == 'Apple Inc.'
    
    def test_simple_usage_example_defaults(self):
        """Test simple usage example with default parameters."""
        with patch('goodgleif.examples.simple_usage_example.CompanyMatcher') as mock_company_matcher:
            mock_gg = MagicMock()
            mock_gg.match_best.return_value = []
            mock_company_matcher.return_value = mock_gg
            
            with patch('builtins.print'):
                result = simple_usage_example()
            
            # Should call with default queries
            expected_queries = ["Apple", "Microsoft", "Tesla", "Goldman Sachs"]
            assert mock_gg.match_best.call_count == len(expected_queries)
    
    def test_main_function(self):
        """Test the main function."""
        with patch('goodgleif.examples.simple_usage_example.simple_usage_example') as mock_example:
            mock_example.return_value = {'test': 'data'}
            
            result = main()
            
            mock_example.assert_called_once()
            assert result == {'test': 'data'}
    
    def test_function_has_docstring(self):
        """Test that the function has a docstring."""
        assert simple_usage_example.__doc__ is not None
        assert "Simple usage example showing how to use GoodGleif" in simple_usage_example.__doc__
