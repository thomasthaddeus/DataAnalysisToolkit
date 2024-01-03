"""data_prep.py

This module provides a class, DataPreprocessor, for preprocessing data. It includes functionalities to standardize or
normalize data, which is an essential step in many data analysis and machine learning workflows.

Extended Summary:
The DataPreprocessor class is designed to preprocess datasets, particularly useful in preparing data for machine learning models.
Currently, it supports data standardization, a process of scaling data such that it has a mean of 0 and a standard deviation of 1.
This is often required to ensure that all features contribute equally to the result and to improve the convergence of algorithms.
"""

from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    """
    A class for preprocessing data for machine learning and data analysis.

    This class provides methods to perform various data preprocessing steps.
    Its primary functionality as of now is to standardize data features, which is crucial in many machine learning algorithms.

    Attributes:
        data (DataFrame): The dataset to be preprocessed.
    """

    def __init__(self, data):
        """
        Initializes the DataPreprocessor object with the dataset.

        Args:
            data (DataFrame): The dataset to be preprocessed. It should be a Pandas DataFrame.
        """
        self.data = data

    def standardize(self, columns):
        """
        Standardizes the specified columns in the dataset.

        This method applies standardization to transform the specified columns in the dataset to have a mean of 0 and
        a standard deviation of 1. It uses sklearn's StandardScaler for this purpose.

        Args:
            columns (list of str): The column names in the dataset that need to be standardized.

        Returns:
            None: The method modifies the dataset in place and does not return anything.
        """
        scaler = StandardScaler()
        self.data[columns] = scaler.fit_transform(self.data[columns])
