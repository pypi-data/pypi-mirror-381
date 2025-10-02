"""
pytest configuration and fixtures for string_date_controller tests
"""
import pytest
from typing import List, Dict, Tuple
from datetime import datetime, timedelta

def generate_date_range(start_date: str, end_date: str) -> List[str]:
    """Generate all dates between start_date and end_date (inclusive)"""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    
    return dates

# Test data constants - ALL DATES
SAMPLE_DATES_2023 = generate_date_range("2023-01-01", "2023-12-31")

SAMPLE_DATES_MULTI_YEAR = (
    generate_date_range("2022-01-01", "2022-12-31") +
    generate_date_range("2023-01-01", "2023-12-31") +
    generate_date_range("2024-01-01", "2024-12-31")
)

SAMPLE_DATES_INCOMPLETE_YEAR = generate_date_range("2023-03-01", "2023-09-30")

# Generate all dates from 2024-12-31 to 2025-07-20
SAMPLE_DATES_CROSS_YEAR_FROM_END_OF_YEAR = generate_date_range("2024-12-31", "2025-07-20")

# Fixtures
@pytest.fixture
def sample_dates_2023() -> List[str]:
    """Sample dates for year 2023"""
    return SAMPLE_DATES_2023

@pytest.fixture
def sample_dates_multi_year() -> List[str]:
    """Sample dates spanning multiple years"""
    return SAMPLE_DATES_MULTI_YEAR

@pytest.fixture
def sample_dates_incomplete_year() -> List[str]:
    """Sample dates for incomplete year (no Jan/Dec)"""
    return SAMPLE_DATES_INCOMPLETE_YEAR

@pytest.fixture
def expected_yearly_pairs_2023() -> Dict[str, Tuple[str, str]]:
    """Expected result for 2023 dates"""
    return {"2023": ("2023-01-01", "2023-12-31")}

@pytest.fixture
def expected_yearly_pairs_multi_year() -> Dict[str, Tuple[str, str]]:
    """Expected result for multi-year dates"""
    return {
        "2022": ("2022-01-01", "2022-12-31"),
        "2023": ("2023-01-01", "2023-12-31"),
        "2024": ("2024-01-01", "2024-12-31")
    }

@pytest.fixture
def expected_yearly_pairs_incomplete() -> Dict[str, Tuple[str, str]]:
    """Expected result for incomplete year"""
    return {"2023": ("2023-03-01", "2023-09-30")}

@pytest.fixture
def sample_dates_cross_year_from_end_of_year() -> List[str]:
    """Sample dates crossing year boundary (2024-12-31 to 2025-07-20) - ALL DATES"""
    return SAMPLE_DATES_CROSS_YEAR_FROM_END_OF_YEAR

@pytest.fixture
def expected_yearly_pairs_cross_year_from_end_of_year() -> Dict[str, Tuple[str, str]]:
    """Expected result for cross-year dates"""
    return {
        "2025": ("2025-01-01", "2025-07-20")
    } 