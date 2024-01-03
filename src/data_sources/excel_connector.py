"""excel_connector.py
_summary_

_extended_summary_

Raises:
    Exception: _description_
    Exception: _description_
    Exception: _description_

Returns:
    _type_: _description_

# Example usage
connector = ExcelConnector('path/to/excel/file.xlsx')
data = connector.load_data(sheet_name='Sheet1', header=0)
all_sheets_data = connector.load_all_sheets()
preview_data = connector.preview_sheet(sheet_name='Sheet1', num_rows=10)
"""

import pandas as pd

class ExcelConnector:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, file_path):
        """
        Initialize the ExcelConnector with the path to an Excel file.

        Args:
            file_path (str): The path to the Excel file.
        """
        self.file_path = file_path

    def load_data(self, sheet_name=0, header=0):
        """
        Load data from a specified sheet in the Excel file.

        Args:
            sheet_name (str or int, optional): The name or index of the sheet to read data from. Defaults to the first sheet.
            header (int, list of int, optional): Row (0-indexed) to use as the header.

        Returns:
            DataFrame: A pandas DataFrame containing the data from the Excel file.
        """
        try:
            return pd.read_excel(self.file_path, sheet_name=sheet_name, header=header)
        except Exception as e:
            raise Exception(f"Error reading Excel file: {e}")

    def load_all_sheets(self):
        """
        Load all sheets from the Excel file.

        Returns:
            dict: A dictionary of DataFrames, with sheet names as keys and DataFrames as values.
        """
        try:
            return pd.read_excel(self.file_path, sheet_name=None)
        except Exception as e:
            raise Exception(f"Error reading Excel file: {e}")

    def preview_sheet(self, sheet_name=0, num_rows=5):
        """
        Preview a few rows from a specified sheet in the Excel file.

        Args:
            sheet_name (str or int, optional): The name or index of the sheet. Defaults to the first sheet.
            num_rows (int, optional): Number of rows to preview. Defaults to 5.

        Returns:
            DataFrame: A pandas DataFrame containing the first few rows from the specified sheet.
        """
        try:
            return pd.read_excel(self.file_path, sheet_name=sheet_name, nrows=num_rows)
        except Exception as e:
            raise Exception(f"Error previewing Excel file: {e}")
