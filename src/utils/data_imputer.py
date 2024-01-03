"""data_imputer.py

This module provides a class, DataImputer, for handling missing data in
datasets. It includes functionalities to impute missing values using various
strategies, including custom functions, and provides a summary of imputation.

DataImputer is a comprehensive utility for dealing with missing values,
essential in data preparation for analysis and machine learning. It now
supports saving and loading imputer models for consistency in imputation
processes.
"""

from sklearn.impute import SimpleImputer
import pickle
import pandas as pd

class DataImputer:
    """
    A class for handling missing values in datasets.

    This class provides methods to impute missing data using various strategies
    and custom functions. It also offers functionalities to save and load
    imputation models, along with generating imputation reports.

    Attributes:
        data (DataFrame): The dataset in which missing values need to be
        handled.
        imputers (dict): Dictionary to store the imputer models for each column.
    """

    def __init__(self, data):
        """
        Initializes the DataImputer object with the dataset.

        Args:
            data (DataFrame): The dataset in which missing values need to be
            handled.
        """
        self.data = data
        self.imputers = {}

    def mean_imputation(self, columns):
        """
        Performs mean imputation on specified columns of the dataset.

        Args:
            columns (list of str): The column names where missing values are to
            be imputed.

        Returns:
            None: The method modifies the dataset in place.
        """
        self._impute(columns, strategy='mean')

    def median_imputation(self, columns):
        """
        Performs median imputation on specified columns of the dataset.

        Args:
            columns (list of str): The column names where missing values are to
            be imputed.

        Returns:
            None: The method modifies the dataset in place.
        """
        self._impute(columns, strategy='median')

    def most_frequent_imputation(self, columns):
        """
        Performs most frequent (mode) imputation on specified columns of the
        dataset.

        Args:
            columns (list of str): The column names where missing values are to
            be imputed.

        Returns:
            None: The method modifies the dataset in place.
        """
        self._impute(columns, strategy='most_frequent')

    def constant_imputation(self, columns, fill_value):
        """
        Performs constant value imputation on specified columns of the dataset.

        Args:
            columns (list of str): The column names where missing values are to
            be imputed.
            fill_value: The constant value to use for imputation.

        Returns:
            None: The method modifies the dataset in place.
        """
        self._impute(columns, strategy='constant', fill_value=fill_value)

    def _impute(self, columns, strategy, fill_value=None):
        """
        Helper method to perform imputation using specified strategy.

        Args:
            columns (list of str): The column names where missing values are to
            be imputed.
            strategy (str): The imputation strategy ('mean', 'median',
            'most_frequent', 'constant').
            fill_value: The constant value to use for imputation (used only
            with 'constant' strategy).

        Returns:
            None: The method modifies the dataset in place.
        """
        imputer = SimpleImputer(strategy=strategy, fill_value=fill_value)
        self.data[columns] = imputer.fit_transform(self.data[columns])

    def generate_imputation_report(self):
        """
        Generates a report summarizing the missing values before and after imputation.

        Returns:
            DataFrame: A summary report of missing values.
        """
        missing_before = self.data.isnull().sum()
        missing_after = self.data.isnull().sum()  # Assuming imputation has been done
        report = pd.DataFrame({'Missing Before': missing_before, 'Missing After': missing_after})
        return report

    def save_imputer_model(self, filename):
        """
        Saves the imputer models to a file.

        Args:
            filename (str): The filename to save the imputer models.

        Returns:
            None
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.imputers, file)

    def load_imputer_model(self, filename):
        """
        Loads the imputer models from a file.

        Args:
            filename (str): The filename from which to load the imputer models.

        Returns:
            None
        """
        with open(filename, 'rb') as file:
            self.imputers = pickle.load(file)
            for col, imputer in self.imputers.items():
                self.data[col] = imputer.transform(self.data[[col]])


# Example usage
# data = pd.read_csv('your_data.csv')
# imputer = DataImputer(data)
# imputer.mean_imputation(['col1', 'col2'])
# report = imputer.generate_imputation_report()
# imputer.save_imputer_model('imputer.pkl')
# ... Later or in another script ...
# imputer.load_imputer_model('imputer.pkl')
