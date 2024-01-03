"""csv_data_generator.py

This module provides a class, CSVDataGenerator, for generating CSV files with
randomly generated data. It is useful for creating test datasets for data
processing and machine learning model testing.

The CSVDataGenerator class is capable of generating a specified number of rows
of data, each containing a mix of random integer, float, date, time, money, and
text values. This is especially useful in scenarios where real data is not
available for testing or development purposes. The class allows for the
customization of the number of rows and the output file name.
"""

import csv
import random
from datetime import datetime, timedelta
import nltk
from nltk.corpus import words

class CSVDataGenerator:
    """
    A class to generate CSV files with random data.

    This class can generate a CSV file filled with random data across various
    field types, including integers, floats, strings, dates, and times. The
    randomness includes the option of generating null values, simulating
    real-world data scenarios.

    Attributes:
        filename (str): The name of the file where the CSV data will be saved.
        num_rows (int): The number of rows of data to generate.
        word_list (list of str): A list of words used for generating random
        text.
    """

    def __init__(self, filename, num_rows=1000):
        """
        Initializes the CSVDataGenerator object with the file name and number
        of rows.

        Args:
            filename (str): The name of the CSV file to be generated.
            num_rows (int, optional): The number of data rows to generate in
            the CSV file. Defaults to 1000.
        """
        self.filename = filename
        self.num_rows = num_rows
        nltk.download("words")
        self.word_list = words.words()

    def random_int(self):
        """
        Generates a random integer.

        Returns:
            int: A random integer between 1 and 1000.
        """
        return random.randint(1, 1000)

    def random_float(self):
        """
        Generates a random float.

        Returns:
            float: A random float rounded to two decimal places, between 1.0
            and 1000.0.
        """
        return round(random.uniform(1.0, 1000.0), 2)

    def random_date(self):
        """
        Generates a random date.

        Returns:
            str: A random date in the format 'YYYY-MM-DD', within the last 20
            years.
        """
        start_date = datetime(2000, 1, 1)
        random_days = random.randint(0, 7300)  # up to 20 years
        return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

    def random_time(self):
        """
        Generates a random time.

        Returns:
            str: A random time in the format 'HH:MM'.
        """
        return f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"

    def random_money(self):
        """
        Generates a random monetary value.

        Returns:
            float: A random monetary value rounded to two decimal places,
            between 1.0 and 1000.0.
        """
        return round(random.uniform(1.0, 1000.0), 2)

    def random_text(self, length=5):
        """
        Generates a random string of words.

        Args:
            length (int, optional): The number of words in the generated
            string. Defaults to 5.

        Returns:
            str: A string composed of 'length' random words.
        """
        return " ".join(random.choice(self.word_list) for _ in range(length))

    def maybe_null(self, value):
        """
        Randomly decides whether to return the provided value or None.

        This function simulates the presence of null values in real-world data.

        Args:
            value (any): The value to potentially return.

        Returns:
            any or None: Either the provided value or None, based on a random
            decision.
        """
        return value if random.random() > 0.004 else None

    def generate_csv(self):
        """
        Generates a CSV file with random data.

        The generated CSV file will contain the specified number of rows, each
        with random data across various field types. The types include integer,
        float, date, time, money, and text fields. Some fields may randomly be
        null.

        Returns:
            None: This method writes to a file and does not return a value.
        """
        with open(
            self.filename, mode="w", newline="", encoding="utf-8"
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [
                    "Integer",
                    "Float",
                    "Text1",
                    "Text2",
                    "Text3",
                    "Text4",
                    "Text5",
                    "Date",
                    "Time",
                    "Money",
                ]
            )
            for _ in range(self.num_rows):
                writer.writerow(
                    [
                        self.maybe_null(self.random_int()),
                        self.maybe_null(self.random_float()),
                        self.maybe_null(self.random_text()),
                        self.maybe_null(self.random_text()),
                        self.maybe_null(self.random_text()),
                        self.maybe_null(self.random_text()),
                        self.maybe_null(self.random_text()),
                        self.maybe_null(self.random_date()),
                        self.maybe_null(self.random_time()),
                        self.maybe_null(self.random_money()),
                    ]
                )


# Usage
generator = CSVDataGenerator("data/gen_test.csv")
generator.generate_csv()
