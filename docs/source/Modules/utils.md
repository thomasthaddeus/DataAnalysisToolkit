# Documentation for `utils` Module of DataAnalysisToolkit

The `utils` module in DataAnalysisToolkit provides utilities for handling common data preprocessing challenges, such as dealing with missing values. This module is essential in preparing datasets for analysis and machine learning.

## Data Imputer (`data_imputer.py`)

### Overview

The `DataImputer` class offers comprehensive functionalities for imputing missing values in datasets. It supports various imputation strategies, including mean, median, most frequent, and constant imputation, and allows for saving and loading imputer models for consistent imputation processes.

### Usage

```python
data = pd.read_csv('your_data.csv')
imputer = DataImputer(data)
imputer.mean_imputation(['col1', 'col2'])
report = imputer.generate_imputation_report()
```

### Methods

- `__init__(self, data)`: Initialize with a dataset to handle missing values.
- `mean_imputation(self, columns)`: Impute missing values in specified columns using the mean.
- `median_imputation(self, columns)`: Impute using the median value.
- `most_frequent_imputation(self, columns)`: Impute using the most frequent value.
- `constant_imputation(self, columns, fill_value)`: Impute using a constant value.
- `generate_imputation_report(self)`: Generate a report summarizing missing values before and after imputation.
- `save_imputer_model(self, filename)`: Save the imputer models to a file for future use.
- `load_imputer_model(self, filename)`: Load imputer models from a file.

### Example

Handling Missing Data and Generating an Imputation Report:

```python
data_imputer = DataImputer(df)
data_imputer.median_imputation(['age', 'salary'])
imputation_report = data_imputer.generate_imputation_report()
print(imputation_report)
```

### Extended Summary

Dealing with missing data is a common challenge in data analysis and machine learning. The `DataImputer` class provides a streamlined and flexible approach to handle missing values in various ways, fitting different types of data and use cases. It also includes functionalities for generating reports on the imputation process and saving/loading models for reproducibility and consistency.

---

The `utils` module is a crucial part of the DataAnalysisToolkit, offering tools that enhance the quality and reliability of data before it undergoes analysis or modeling. The `DataImputer` class, in particular, ensures that datasets are properly prepared, handling one of the most common preprocessing tasks efficiently.
