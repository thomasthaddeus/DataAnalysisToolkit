import pytest
import pandas as pd
from dataanalysistoolkit.interfaces.excel_connector import ExcelConnector

# Create a sample Excel file for testing
@pytest.fixture(scope="module")
def create_sample_excel(tmp_path_factory):
    file_path = tmp_path_factory.mktemp("data") / "test.xlsx"
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['x', 'y', 'z']
    })
    df.to_excel(file_path, index=False)
    return file_path

def test_load_data(create_sample_excel):
    connector = ExcelConnector(str(create_sample_excel))
    data = connector.load_data()

    # Check if the data is loaded correctly
    assert not data.empty
    assert list(data.columns) == ['A', 'B']
    assert (data['A'] == [1, 2, 3]).all()
    assert (data['B'] == ['x', 'y', 'z']).all()

def test_load_data_with_specific_sheet(create_sample_excel):
    connector = ExcelConnector(str(create_sample_excel))
    data = connector.load_data(sheet_name='Sheet1')

    # Check if data from the specified sheet is loaded correctly
    assert not data.empty
    assert list(data.columns) == ['A', 'B']

# Additional tests for other methods or functionalities can be added here
