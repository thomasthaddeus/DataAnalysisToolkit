import pytest
import pandas as pd
from src.integrators.data_integrator import DataIntegrator

@pytest.fixture
def sample_dataframes():
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})
    return df1, df2

def test_concatenate_data(sample_dataframes):
    df1, df2 = sample_dataframes
    integrator = DataIntegrator()
    integrator.add_data(df1)
    integrator.add_data(df2)

    result = integrator.concatenate_data()
    assert len(result) == len(df1) + len(df2)
    assert list(result.columns) == list(df1.columns)

def test_merge_data(sample_dataframes):
    df1 = pd.DataFrame({'key': [1, 2, 3], 'value1': [4, 5, 6]})
    df2 = pd.DataFrame({'key': [1, 2, 3], 'value2': [7, 8, 9]})
    integrator = DataIntegrator()
    integrator.add_data(df1)
    integrator.add_data(df2)

    result = integrator.merge_data(on='key')
    assert len(result) == len(df1)
    assert list(result.columns) == ['key', 'value1', 'value2']
    assert all(result['key'] == df1['key'])

# Additional tests for other methods or scenarios can be added here
