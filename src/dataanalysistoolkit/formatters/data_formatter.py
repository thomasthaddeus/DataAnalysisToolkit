"""data_formatter.py
_summary_

_extended_summary_

# Example usage
formatter = DataFormatter(df)
formatter.standardize_dates('date_column')
formatter.categorize_columns(['category_column1', 'category_column2'])
formatter.normalize_numeric(['numeric_column1', 'numeric_column2'])
formatter = DataFormatter(df)
formatter.fill_missing_values('some_column', fill_value=0)
formatter.encode_categorical_variables(['category_column1', 'category_column2'])
formatter.custom_transform('numeric_column', lambda x: x ** 2)
"""

import pandas as pd


class DataFormatter:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, data):
        """
        Initialize the DataFormatter with a DataFrame.

        Args:
            data (DataFrame): The pandas DataFrame to be formatted.
        """
        self.data = data

    def standardize_dates(self, date_column, date_format='%Y-%m-%d'):
        """
        Standardize the format of a date column in the DataFrame.

        Args:
            date_column (str): The name of the column containing date information.
            date_format (str, optional): The target date format. Defaults to '%Y-%m-%d'.

        Returns:
            None: The method modifies the DataFrame in place.
        """
        self.data[date_column] = pd.to_datetime(self.data[date_column]).dt.strftime(date_format)

    def categorize_columns(self, columns):
        """
        Convert specified columns to categorical data types.

        Args:
            columns (list of str): A list of column names to be converted to categorical type.

        Returns:
            None: The method modifies the DataFrame in place.
        """
        for col in columns:
            self.data[col] = self.data[col].astype('category')

    def normalize_numeric(self, numeric_columns):
        """
        Normalize numeric columns in the DataFrame.

        Args:
            numeric_columns (list of str): A list of column names containing numeric data.

        Returns:
            None: The method modifies the DataFrame in place.
        """
        for col in numeric_columns:
            self.data[col] = (self.data[col] - self.data[col].mean()) / self.data[col].std()

    def fill_missing_values(self, column, fill_value=None, method=None):
        """
        Fill missing values in a specified column.

        Args:
            column (str): The name of the column to fill missing values.
            fill_value (any, optional): The value to use for filling missing values.
            method (str, optional): The method to use for filling gaps ('ffill', 'bfill').

        Returns:
            None: The method modifies the DataFrame in place.
        """
        if method:
            self.data[column].fillna(method=method, inplace=True)
        else:
            self.data[column].fillna(fill_value, inplace=True)

    def encode_categorical_variables(self, columns):
        """
        Encode categorical variables using one-hot encoding.

        Args:
            columns (list of str): A list of column names to be one-hot encoded.

        Returns:
            None: The method modifies the DataFrame in place.
        """
        self.data = pd.get_dummies(self.data, columns=columns)

    def custom_transform(self, column, transform_func):
        """
        Apply a custom transformation function to a specified column.

        Args:
            column (str): The name of the column to apply the transformation.
            transform_func (function): The transformation function to apply.

        Returns:
            None: The method modifies the DataFrame in place.
        """
        self.data[column] = self.data[column].apply(transform_func)

    # Additional methods for other formatting tasks can be added here.
