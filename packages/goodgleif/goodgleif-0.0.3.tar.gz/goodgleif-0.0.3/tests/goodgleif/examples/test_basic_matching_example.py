"""
Tests for the basic_matching_example module.
"""

import pytest
from unittest.mock import patch, MagicMock

from goodgleif.examples.basic_matching_example import basic_matching_example, main


class TestBasicMatchingExample:
    """Test the basic matching example function."""
    
    @patch('goodgleif.examples.basic_matching_example.CompanyMatcher')
    def test_basic_matching_example(self, mock_company_matcher):
        """Test basic matching example with mocked CompanyMatcher."""
        # Setup mock
        mock_gg = MagicMock()
        mock_gg.match_best.return_value = [
            {
                'original_name': 'Apple Inc.',
                'canonical_name': 'apple inc',
                'lei': 'HWUPKR0MPOU8FGXBT394',
                'country': 'US',
                'score': 95.5
            },
            {
                'original_name': 'Apple Computer Inc.',
                'canonical_name': 'apple computer inc',
                'lei': 'HWUPKR0MPOU8FGXBT395',
                'country': 'US',
                'score': 88.2
            }
        ]
        mock_company_matcher.return_value = mock_gg
        
        # Test the function
        with patch('builtins.print'):  # Suppress print output
            result = basic_matching_example("Apple", limit=3, min_score=70)
        
        # Verify calls
        mock_gg.load_data.assert_called_once()
        mock_gg.match_best.assert_called_once_with("Apple", limit=3, min_score=70)
        
        # Verify result
        assert len(result) == 2
        assert result[0]['original_name'] == 'Apple Inc.'
        assert result[1]['original_name'] == 'Apple Computer Inc.'
    
    def test_basic_matching_example_defaults(self):
        """Test basic matching example with default parameters."""
        with patch('goodgleif.examples.basic_matching_example.CompanyMatcher') as mock_company_matcher:
            mock_gg = MagicMock()
            mock_gg.match_best.return_value = []
            mock_company_matcher.return_value = mock_gg
            
            with patch('builtins.print'):
                result = basic_matching_example()
            
            mock_gg.match_best.assert_called_once_with("Apple", limit=3, min_score=70)
    
    def test_main_function(self):
        """Test the main function."""
        with patch('goodgleif.examples.basic_matching_example.basic_matching_example') as mock_example:
            mock_example.return_value = [{'test': 'data'}]
            
            result = main()
            
            mock_example.assert_called_once()
            assert result == [{'test': 'data'}]
    
    def test_function_has_docstring(self):
        """Test that the function has a docstring."""
        assert basic_matching_example.__doc__ is not None
        assert "Simple example of basic company matching" in basic_matching_example.__doc__
