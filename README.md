# DataAnalyzer

DataAnalyzer is a Python-based data analysis tool designed to streamline various data analysis tasks. It provides the ability to load data from CSV files, perform statistical calculations, detect outliers, clean data, and visualize data.

## Features

- Load data from CSV files
- Calculate statistics (mean, median, mode, and trimmed mean) for a specified column
- Detect outliers in a specified column using the z-score method
- Handle missing values (either by dropping or filling them)
- Drop duplicate rows from the DataFrame
- Encode categorical features in the DataFrame
- Split the data into training and testing sets for machine learning tasks
- Plot a histogram for a specified column
- Export the cleaned and processed data to a new CSV file

## Key Features

1. **Statistical Calculations**: It provides easy methods to calculate common statistics like mean, median, mode, and trimmed mean of any given column in the data.
2. **Outlier Detection**: It contains methods to identify outliers in the data using the z-score method.
3. **Data Cleaning**: It offers functionalities to handle missing values (either by dropping or filling them), drop duplicate rows, and encode categorical features.
4. **Data Splitting**: It includes a method to split the data into training and testing sets, which is often required in machine learning tasks.
5. **Visualization**: It provides the ability to plot histograms of any column in the data, aiding in visual data analysis.
6. **Data Export**: It allows users to export the analyzed data to a new CSV file.

This tool is highly beneficial for data analysts and data scientists, offering them a simplified interface for conducting preliminary data analysis. It can also be incorporated into larger data processing pipelines, serving as a preprocessing step for machine learning models.

## Usage

```python
from data_analyzer import DataAnalyzer

# Initialize the analyzer with the path to a CSV file
analyzer = DataAnalyzer('path_to_your_file.csv')

# Calculate the mean, median, mode, and trimmed mean of a column
statistics = analyzer.calculate_budget_statistics('column_name')
print(statistics)

# Detect outliers in a column using the z-score method
outliers = analyzer.detect_outliers('column_name')
print(outliers)

# Handle missing values in a column
analyzer.handle_missing_values('column_name', strategy='fill', fill_value=0)

# Drop duplicate rows in the DataFrame
analyzer.drop_duplicates()

# Encode categorical features in the DataFrame
analyzer.encode_categorical_features()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = analyzer.split_data('target_column')

# Plot a histogram of a column
analyzer.plot_data('column_name')

# Export the data to a CSV file
analyzer.export_data('new_file.csv')
```

## Installation

To install `DataAnalyzer`, you can use pip:

```python
pip install dataanalyzer
```

## License

This project is licensed under the terms of the [MIT license](./License).
