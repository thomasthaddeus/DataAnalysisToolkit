### Documentation for `formatters` Module of DataAnalysisToolkit

The `formatters` module in DataAnalysisToolkit offers tools for transforming and standardizing data in a DataFrame. It's designed to prepare your data for analysis, ensuring consistency and quality.

#### Data Formatter (`data_formatter.py`)

##### Overview

The `DataFormatter` class is a versatile tool for performing various data formatting tasks on a pandas DataFrame. It can standardize date formats, normalize numeric data, categorize columns, and more.

##### Usage

```python
formatter = DataFormatter(df)
formatter.standardize_dates('date_column')
formatter.categorize_columns(['category_column1', 'category_column2'])
formatter.normalize_numeric(['numeric_column1', 'numeric_column2'])
```

##### Methods

- `__init__(self, data)`: Initialize the formatter with a DataFrame.
- `standardize_dates(self, date_column, date_format='%Y-%m-%d')`: Standardize the format of a date column.
- `categorize_columns(self, columns)`: Convert specified columns to categorical data types for efficiency.
- `normalize_numeric(self, numeric_columns)`: Normalize numeric columns by scaling to a mean of 0 and standard deviation of 1.
- `fill_missing_values(self, column, fill_value=None, method=None)`: Fill missing values in a column either with a specified value or using a method like forward-fill or backward-fill.
- `encode_categorical_variables(self, columns)`: Perform one-hot encoding on categorical variables to transform them into a format suitable for machine learning models.
- `custom_transform(self, column, transform_func)`: Apply a custom transformation function to a specified column, allowing for flexible data transformations.

##### Examples

Here are some examples demonstrating how to use the `DataFormatter` class:

Standardizing a Date Column:

```python
formatter = DataFormatter(df)
formatter.standardize_dates('date_column')
```

Normalizing Numeric Data:

```python
formatter.normalize_numeric(['age', 'income'])
```

Encoding Categorical Variables:

```python
formatter.encode_categorical_variables(['gender', 'occupation'])
```

Custom Transformations:

```python
formatter.custom_transform('price', lambda x: x * 1.2)
```

---

The `formatters` module is essential for ensuring data consistency and quality, making it easier to perform reliable analysis. By providing a range of methods for data transformation, this module helps streamline the preprocessing stage of your data analysis projects.
