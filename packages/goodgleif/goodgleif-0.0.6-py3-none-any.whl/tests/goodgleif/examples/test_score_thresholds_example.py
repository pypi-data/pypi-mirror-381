"""
Tests for the score_thresholds_example module.
"""

import pytest
from unittest.mock import patch, MagicMock

from goodgleif.examples.score_thresholds_example import score_thresholds_example, main


class TestScoreThresholdsExample:
    """Test the score thresholds example function."""
    
    @patch('goodgleif.examples.score_thresholds_example.CompanyMatcher')
    def test_score_thresholds_example(self, mock_company_matcher):
        """Test score thresholds example with mocked CompanyMatcher."""
        # Setup mock
        mock_gg = MagicMock()
        mock_gg.match_best.side_effect = [
            [{'original_name': 'Apple Inc.', 'score': 95.5}],  # score >= 90
            [{'original_name': 'Apple Inc.', 'score': 95.5}, {'original_name': 'Apple Computer Inc.', 'score': 85.2}],  # score >= 80
            [{'original_name': 'Apple Inc.', 'score': 95.5}, {'original_name': 'Apple Computer Inc.', 'score': 85.2}, {'original_name': 'Apple Corp.', 'score': 75.1}],  # score >= 70
            [{'original_name': 'Apple Inc.', 'score': 95.5}, {'original_name': 'Apple Computer Inc.', 'score': 85.2}, {'original_name': 'Apple Corp.', 'score': 75.1}, {'original_name': 'Apple Ltd.', 'score': 65.8}]  # score >= 60
        ]
        mock_company_matcher.return_value = mock_gg
        
        # Test the function
        with patch('builtins.print'):
            result = score_thresholds_example("Apple", [90, 80, 70, 60])
        
        # Verify calls
        assert mock_gg.match_best.call_count == 4
        mock_gg.match_best.assert_any_call("Apple", limit=3, min_score=90)
        mock_gg.match_best.assert_any_call("Apple", limit=3, min_score=80)
        mock_gg.match_best.assert_any_call("Apple", limit=3, min_score=70)
        mock_gg.match_best.assert_any_call("Apple", limit=3, min_score=60)
        
        # Verify result structure
        assert 90 in result
        assert 80 in result
        assert 70 in result
        assert 60 in result
        assert len(result[90]) == 1
        assert len(result[80]) == 2
        assert len(result[70]) == 3
        assert len(result[60]) == 4
    
    def test_score_thresholds_example_defaults(self):
        """Test score thresholds example with default parameters."""
        with patch('goodgleif.examples.score_thresholds_example.CompanyMatcher') as mock_company_matcher:
            mock_gg = MagicMock()
            mock_gg.match_best.return_value = []
            mock_company_matcher.return_value = mock_gg
            
            with patch('builtins.print'):
                result = score_thresholds_example()
            
            # Should call with default thresholds [90, 80, 70, 60]
            assert mock_gg.match_best.call_count == 4
    
    def test_main_function(self):
        """Test the main function."""
        with patch('goodgleif.examples.score_thresholds_example.score_thresholds_example') as mock_example:
            mock_example.return_value = {'test': 'data'}
            
            result = main()
            
            mock_example.assert_called_once()
            assert result == {'test': 'data'}
    
    def test_function_has_docstring(self):
        """Test that the function has a docstring."""
        assert score_thresholds_example.__doc__ is not None
        assert "Example showing how score thresholds affect results" in score_thresholds_example.__doc__
