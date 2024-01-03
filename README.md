# Data Analysis Toolkit

[![Upload Python Package](https://github.com/thomasthaddeus/DataAnalysisToolkit/actions/workflows/python-publish.yml/badge.svg)](https://github.com/thomasthaddeus/DataAnalysisToolkit/actions/workflows/python-publish.yml)

DataAnalysisToolkit is a comprehensive Python package offering a suite of tools designed for efficient data analysis. This toolkit simplifies tasks such as loading CSV data, performing statistical analysis, cleaning data, and visualizing results. It's an ideal tool for data analysts, scientists, and anyone looking to dive into data exploration and machine learning.

## Features

- **Data Loading**: Load data directly from CSV files into a Python environment.
- **Statistical Analysis**: Perform calculations like mean, median, mode, and trimmed mean.
- **Outlier Detection**: Identify outliers using the z-score method.
- **Data Cleaning**: Handle missing values, drop duplicates, and encode categorical data.
- **Data Splitting**: Easily split data into training and testing sets for machine learning models.
- **Data Visualization**: Create histograms and other plots to explore data visually.
- **Data Export**: Export cleaned and processed data back into CSV format.

## Enhanced Functionalities

- **Advanced Visualization**: Utilize a dedicated visualizer for creating a variety of insightful data plots.
- **Feature Engineering**: Enhance your data with new, informative features.
- **Model Evaluation**: Assess the performance of machine learning models.
- **Report Generation**: Automatically generate comprehensive HTML reports with summaries and visualizations.
- **Data Imputation**: Implement advanced imputation techniques to handle missing data.

This toolkit is an asset for conducting preliminary data analysis, and it seamlessly integrates into larger data processing workflows.

## Getting Started

Here's how you can get started with DataAnalysisToolkit:

```python
from data_analysis_toolkit import DataAnalysisToolkit

# Initialize the analyzer with the path to a CSV file
analyzer = DataAnalysisToolkit('../data/test.csv')


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

Install DataAnalysisToolkit using pip:

```bash
pip install dataanalysistoolkit
```

## Documentation

For detailed documentation, examples, and usage guides, please visit [DataAnalysisToolkit Documentation](https://github.com/thomasthaddeus/DataAnalysisToolkit/wiki).

## Contributing

Contributions are welcome! For guidelines on how to contribute, please refer to our [Contribution Guide](https://github.com/thomasthaddeus/DataAnalysisToolkit/CONTRIBUTING.md).

## License

DataAnalysisToolkit is open-sourced under the MIT License. For more details, see the [LICENSE](./LICENSE) file.

---

Developed with ❤ by the DataAnalysisToolkit Team.
