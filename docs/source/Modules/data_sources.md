# Documentation for `data_sources` Module of DataAnalysisToolkit

The `data_sources` module of DataAnalysisToolkit provides a suite of connectors for importing data from various sources like APIs, Excel files, and SQL databases. Each connector is designed to simplify the process of fetching and loading data into a format suitable for analysis in Python.

## API Connector (`api_connector.py`)

### Overview

The `APIConnector` class allows you to easily fetch data from web APIs. It handles the complexities of making HTTP requests and processing responses.

### Usage

```python
connector = APIConnector('https://api.example.com', auth=('username', 'password'))
response = connector.get('endpoint', params={'key': 'value'})
print(response.json())
```

### Methods

- `__init__(self, base_url, auth=None)`: Initialize the connector with API base URL and optional authentication.
- `get(self, endpoint, params=None)`: Perform a GET request to the specified endpoint.
- `post(self, endpoint, data=None, json=None)`: Send a POST request with provided data.
- `put(self, endpoint, data=None, json=None)`: Send a PUT request to update resources.
- `delete(self, endpoint, params=None)`: Send a DELETE request to remove resources.
- `patch(self, endpoint, data=None, json=None)`: Send a PATCH request for partial updates.

---

## Excel Connector (`excel_connector.py`)

### Overview

The `ExcelConnector` class provides functionality to read data from Excel files. It supports different sheets and custom formats.

### Usage

```python
connector = ExcelConnector('path/to/excel/file.xlsx')
data = connector.load_data(sheet_name='Sheet1')
```

### Methods

- `__init__(self, file_path)`: Initialize the connector with the path to an Excel file.
- `load_data(self, sheet_name=0, header=0)`: Load data from a specified sheet in the Excel file.
- `load_all_sheets(self)`: Load all sheets from the Excel file into a dictionary of DataFrames.
- `preview_sheet(self, sheet_name=0, num_rows=5)`: Preview a few rows from a specified sheet.

---

## SQL Connector (`sql_connector.py`)

### Overview

The `SQLConnector` class enables you to connect to SQL databases, execute queries, and retrieve results in a DataFrame format.

### Usage

```python
connector = SQLConnector('postgresql://user:password@localhost:5432/mydatabase')
data = connector.query_data('SELECT * FROM my_table')
```

### Methods

- `__init__(self, db_uri)`: Initialize the connector with a database URI.
- `query_data(self, query)`: Execute a SQL query and return the results.
- `insert_data(self, df, table_name, if_exists='append')`: Insert data from a DataFrame into a SQL table.
- `update_data(self, query)`: Execute a SQL query to update data in the database.

---

Each connector is designed to handle specific data source types, providing a consistent and efficient way to import data into your Python environment for further processing and analysis.
