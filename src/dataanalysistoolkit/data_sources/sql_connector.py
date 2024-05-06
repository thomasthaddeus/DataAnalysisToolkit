"""data_sources/sql_connector.py

This module provides a SQLConnector class for connecting to and interacting
with a SQL database. The SQLConnector simplifies executing queries and
performing database operations like inserting and updating data, using
SQLAlchemy for database connections and pandas for handling query results.

Raises:
    Exception: Raised when a SQL query execution fails.
    Exception: Raised when inserting data into a database fails.
    Exception: Raised when updating data in the database fails.

Returns:
    DataFrame: Returns the result of SQL queries as pandas DataFrames.

Example usage:
connector = SQLConnector('postgresql://user:password@localhost:5432/mydatabase')
data = connector.query_data('SELECT * FROM my_table')
connector.insert_data(df, 'my_table')
connector.update_data('UPDATE my_table SET column = value WHERE condition')
"""

import logging
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import pandas as pd
from pandas.errors import DatabaseError

logger = logging.getLogger(__name__)


class SQLConnectorError(Exception):
    """Custom exception class that formats the error message along with query details."""

    def __init__(self, original_exception, query=None):
        self.original_exception = original_exception
        self.query = query
        super().__init__(self.__str__())

    def __str__(self):
        """Return the formatted exception message."""
        return f"Error executing query: {self.query}. Error: {self.original_exception}"


class WrappedException(Exception):
    def __init__(self, err, context_message):
        self.err = err
        self.context_message = context_message
        super().__init__(str(self))

    def __str__(self):
        return f"{self.context_message}. Original Error: {self.err}"


class SQLConnector:
    """
    Provides methods to connect to a SQL database and execute queries, insert,
    and update data.

    This class uses SQLAlchemy to manage database connections and pandas to
    convert SQL query results into DataFrame objects for easier manipulation
    and analysis.
    """

    def __init__(self, db_uri):
        """
        Initializes a new instance of the SQLConnector class with a specific database URI.

        Args:
            db_uri (str): The connection string for the database, typically
            including the type of database, username, password, host, and
            database name.
        """
        self.db_uri = db_uri
        self.engine = sqlalchemy.create_engine(db_uri)
        self._logger = None

    @property
    def logger(self):
        """
        Returns a logger instance for this class. The logger is created upon
        first access.
        """
        if self._logger is None:
            self._logger = logging.getLogger(__name__)
        return self._logger

    def __repr__(self) -> str:
        return f"SQLConnector(db_uri={self.db_uri})"

    def query_data(self, query):
        """
        Execute a SQL query and return the results as a DataFrame.

        Args:
            query (str): The SQL query to execute.

        Returns:
            DataFrame: The result of the SQL query.

        Raises:
            DatabaseError: An error occurred when querying the database.
        """
        self.logger.info("Executing query: %s", query)
        try:
            with self.engine.connect() as connection:
                return pd.DataFrame(pd.read_sql_query(query, connection))
        except (SQLAlchemyError, DatabaseError) as e:
            self.logger.error("Error executing query: %s. Error: %s", query, str(e))
            raise SQLConnectorError(e, query) from e

    def insert_data(self, df, table_name, if_exists="append"):
        """
        Insert data from a DataFrame into a SQL table.

        Args:
            df (DataFrame): The DataFrame to insert into the table.
            table_name (str): The name of the target table.
            if_exists (str): What to do if the table already exists. Options
              are 'fail', 'replace', 'append'.

        Returns:
            None

        Raises:
            SQLConnectorError: Custom error with detailed information.
        """
        try:
            df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
        except (SQLAlchemyError, DatabaseError) as e:
            raise SQLConnectorError(e, f"INSERT INTO {table_name}") from e

    def update_data(self, query):
        """
        Execute a SQL query to update data in the database.

        Args:
            query (str): The SQL query to execute.

        Returns:
            None

        Raises:
            SQLConnectorError: Custom error with detailed information.
        """
        try:
            with self.engine.connect() as connection:
                connection.execute(query)
        except (SQLAlchemyError, OperationalError) as e:
            raise SQLConnectorError(e, query) from e

    def start_transaction(self):
        """Starts a new transaction."""
        connection = self.engine.connect()
        transaction = connection.begin()
        return connection, transaction

    def end_transaction(self, transaction, operation="commit"):
        """Ends the transaction with either a commit or rollback."""
        if operation == "commit":
            transaction.commit()
        else:
            transaction.rollback()

    def bulk_insert(self, data, table_name):
        """Inserts data in bulk to the specified table."""
        self.engine.execute(table_name.insert(), data)

    def create_table(self, create_statement):
        """Creates a table in the database."""
        self.engine.execute(create_statement)

    def drop_table(self, table_name):
        """Drops a table from the database."""
        self.engine.execute(f"DROP TABLE IF EXISTS {table_name}")

    def set_pooling_options(self, pool_size=5, max_overflow=10, timeout=30):
        """Set options for the SQLAlchemy connection pool.

        Args:
            pool_size (int): The size of the pool to be maintained.
            max_overflow (int): The maximum number of connections to create above `pool_size`.
            timeout (int): The number of seconds to wait before giving up on returning a connection.
        """
        # Dispose the old engine and create a new one with updated settings
        self.engine.dispose()
        self.engine = sqlalchemy.create_engine(
            self.db_uri,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_timeout=timeout,
        )

    def execute_large_query_in_batches(self, query, batch_size=1000):
        """Execute a large SQL query in batches.

        Args:
            query (str): The SQL query to execute.
            batch_size (int): The number of rows to fetch per batch.

        Yields:
            DataFrame: A batch of the result set as a pandas DataFrame.
        """
        with self.engine.connect() as conn:
            result_proxy = conn.execution_options(stream_results=True).execute(
                query
            )
            while True:
                batch = result_proxy.fetchmany(batch_size)
                if not batch:
                    break
                yield pd.DataFrame(batch)

    def safe_transaction(self):
        """Provide a context manager for safe transactions."""
        connection = self.engine.connect()
        transaction = connection.begin()
        try:
            yield connection
            transaction.commit()
        except:
            transaction.rollback()
            raise
        finally:
            connection.close()
