"""
Tests for yearly dates collection functionality
"""
import pytest
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from string_date_controller.timeseries_dates_application.yearly_dates_collector import get_all_data_yearly_date_pairs


def test__get_all_data_yearly_date_pairs__cross_year_from_end_of_year(
    sample_dates_cross_year_from_end_of_year, 
    expected_yearly_pairs_cross_year_from_end_of_year
):
    """Test cross-year case from end of year to middle of next year"""
    result = get_all_data_yearly_date_pairs(sample_dates_cross_year_from_end_of_year)
    assert result == expected_yearly_pairs_cross_year_from_end_of_year 