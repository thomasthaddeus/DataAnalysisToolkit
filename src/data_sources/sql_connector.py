"""sql_connector.py
_summary_

_extended_summary_

Raises:
    Exception: _description_
    Exception: _description_
    Exception: _description_

Returns:
    _type_: _description_

# Example usage
connector = SQLConnector('postgresql://user:password@localhost:5432/mydatabase')
data = connector.query_data('SELECT * FROM my_table')
connector.insert_data(df, 'my_table')
connector.update_data('UPDATE my_table SET column = value WHERE condition')
"""

import pandas as pd
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class SQLConnector:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, db_uri):
        """
        Initialize the SQLConnector with the database URI.

        Args:
            db_uri (str): The database URI.
        """
        self.db_uri = db_uri
        self.engine = sqlalchemy.create_engine(db_uri)

    def query_data(self, query):
        """
        Execute a SQL query and return the results as a DataFrame.

        Args:
            query (str): The SQL query to execute.

        Returns:
            DataFrame: The result of the SQL query.
        """
        try:
            with self.engine.connect() as connection:
                return pd.read_sql_query(query, connection)
        except SQLAlchemyError as e:
            raise Exception(f"Error executing query: {e}")

    def insert_data(self, df, table_name, if_exists='append'):
        """
        Insert data from a DataFrame into a SQL table.

        Args:
            df (DataFrame): The DataFrame to insert into the table.
            table_name (str): The name of the target table.
            if_exists (str): What to do if the table already exists. Options are 'fail', 'replace', 'append'.

        Returns:
            None
        """
        try:
            df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
        except SQLAlchemyError as e:
            raise Exception(f"Error inserting data: {e}")

    def update_data(self, query):
        """
        Execute a SQL query to update data in the database.

        Args:
            query (str): The SQL query to execute.

        Returns:
            None
        """
        try:
            with self.engine.connect() as connection:
                connection.execute(query)
        except SQLAlchemyError as e:
            raise Exception(f"Error updating data: {e}")

    # Additional methods for other database interactions can be added here.
