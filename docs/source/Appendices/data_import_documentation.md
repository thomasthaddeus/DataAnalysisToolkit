# Data Import Documentation

## Overview

The Data Import module of the DataAnalysisToolkit provides functionalities to import data from various sources such as Excel files, SQL databases, and APIs. It is designed to simplify the process of data collection and integration for analysis and machine learning tasks.

## Features

- **Excel Connector**: Import data from Excel files (.xlsx, .xls).
- **SQL Connector**: Connect and import data from SQL databases like MySQL, PostgreSQL, etc.
- **API Connector**: Fetch data from various APIs with handling for authentication and rate-limiting.
- **Data Integrator**: Merge or concatenate data from different sources into a unified DataFrame.
- **Data Formatter**: Standardize and transform the imported data into a consistent format.

## Getting Started

### Excel Connector

To import data from Excel files:

```python
from data_sources.excel_connector import ExcelConnector

connector = ExcelConnector('path/to/excel/file.xlsx')
data = connector.load_data(sheet_name='Sheet1')
```

### SQL Connector

For SQL databases:

```python
from data_sources.sql_connector import SQLConnector

connector = SQLConnector('database_URI')
data = connector.query_data('SELECT * FROM table_name')
```

### API Connector

To fetch data from an API:

```python
from data_sources.api_connector import APIConnector

connector = APIConnector('https://api.example.com', auth=('username', 'password'))
response = connector.get('endpoint')
```

### Data Integrator

Merge or concatenate data from multiple sources:

```python
from integrators.data_integrator import DataIntegrator

integrator = DataIntegrator()
integrator.add_data(data_from_excel)
integrator.add_data(data_from_sql)
combined_data = integrator.concatenate_data()
```

### Data Formatter

Standardize or transform the data:

```python
from formatters.data_formatter import DataFormatter

formatter = DataFormatter(combined_data)
formatter.standardize_dates('date_column')
formatter.normalize_numeric(['numeric_column'])
```

## Error Handling

The toolkit includes error handling for common issues encountered during data import, such as file not found, invalid format, or connection issues. Ensure to handle exceptions in your implementation to maintain robustness.

## Examples

Refer to the `examples` directory for detailed examples of using each connector and integrating data from multiple sources.

## Contribution

Contributions to enhance the data import module, such as adding new connectors or improving existing functionalities, are welcome. Please refer to the contribution guidelines for more details.
