"""
Pytest configuration and fixtures for DataX tests.
"""

import pytest
import pandas as pd
import numpy as np
from typing import Dict, Any
import tempfile
import os


@pytest.fixture
def sample_dataframe():
    """Create a sample DataFrame for testing."""
    np.random.seed(42)
    data = {
        'numeric_col': np.random.normal(100, 15, 100),
        'categorical_col': np.random.choice(['A', 'B', 'C'], 100),
        'date_col': pd.date_range('2023-01-01', periods=100, freq='D'),
        'missing_col': np.random.normal(50, 10, 100),
        'outlier_col': np.random.normal(0, 1, 100),
        'duplicate_col': np.random.choice([1, 2, 3, 4, 5], 100)
    }
    
    # Add some missing values
    data['missing_col'][10:20] = np.nan
    data['numeric_col'][5:8] = np.nan
    
    # Add some outliers
    data['outlier_col'][0] = 100
    data['outlier_col'][1] = -100
    
    # Add some duplicates
    data['duplicate_col'][50:60] = 1
    
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def sample_series():
    """Create a sample Series for testing."""
    np.random.seed(42)
    return pd.Series(np.random.normal(0, 1, 50), name='test_series')


@pytest.fixture
def messy_dataframe():
    """Create a messy DataFrame for testing cleaning functions."""
    np.random.seed(42)
    data = {
        'id': range(1, 101),
        'name': [f'Person_{i}' for i in range(1, 101)],
        'age': np.random.randint(18, 80, 100),
        'salary': np.random.normal(50000, 15000, 100),
        'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], 100),
        'score': np.random.uniform(0, 100, 100)
    }
    
    # Add missing values
    data['age'][10:15] = np.nan
    data['salary'][20:25] = np.nan
    data['department'][30:35] = np.nan
    
    # Add duplicates
    data['id'][50:55] = range(1, 6)  # Duplicate IDs
    
    # Add outliers
    data['salary'][0] = 1000000  # Extreme outlier
    data['score'][1] = -50  # Negative score (invalid)
    
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def time_series_data():
    """Create time series data for testing."""
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=365, freq='D')
    values = np.cumsum(np.random.normal(0, 1, 365)) + 100
    
    df = pd.DataFrame({
        'date': dates,
        'value': values,
        'category': np.random.choice(['A', 'B', 'C'], 365)
    })
    
    return df


@pytest.fixture
def correlation_data():
    """Create data with known correlations for testing."""
    np.random.seed(42)
    n = 100
    
    # Create correlated variables
    x1 = np.random.normal(0, 1, n)
    x2 = 0.8 * x1 + 0.6 * np.random.normal(0, 1, n)  # Strong positive correlation
    x3 = -0.7 * x1 + 0.7 * np.random.normal(0, 1, n)  # Strong negative correlation
    x4 = np.random.normal(0, 1, n)  # No correlation
    
    df = pd.DataFrame({
        'var1': x1,
        'var2': x2,
        'var3': x3,
        'var4': x4,
        'category': np.random.choice(['Group1', 'Group2'], n)
    })
    
    return df


@pytest.fixture
def temp_file():
    """Create a temporary file for testing file operations."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        # Write sample data
        f.write('col1,col2,col3\n')
        f.write('1,2,3\n')
        f.write('4,5,6\n')
        f.write('7,8,9\n')
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def validation_rules():
    """Create validation rules for testing."""
    return {
        "age_range": {
            "type": "range",
            "column": "age",
            "min": 18,
            "max": 80
        },
        "salary_positive": {
            "type": "range",
            "column": "salary",
            "min": 0
        },
        "unique_id": {
            "type": "unique",
            "column": "id"
        }
    }


@pytest.fixture
def mock_data():
    """Create mock data for various testing scenarios."""
    return {
        "empty_df": pd.DataFrame(),
        "single_row_df": pd.DataFrame({'col1': [1], 'col2': [2]}),
        "single_col_df": pd.DataFrame({'col1': [1, 2, 3, 4, 5]}),
        "all_nan_df": pd.DataFrame({'col1': [np.nan, np.nan], 'col2': [np.nan, np.nan]}),
        "mixed_types_df": pd.DataFrame({
            'int_col': [1, 2, 3],
            'float_col': [1.1, 2.2, 3.3],
            'str_col': ['a', 'b', 'c'],
            'bool_col': [True, False, True],
            'date_col': pd.date_range('2023-01-01', periods=3)
        })
    }


# Pytest markers
def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")
    config.addinivalue_line("markers", "cleaning: marks tests for cleaning module")
    config.addinivalue_line("markers", "stats: marks tests for stats module")
    config.addinivalue_line("markers", "viz: marks tests for visualization module")
    config.addinivalue_line("markers", "cli: marks tests for CLI module")
