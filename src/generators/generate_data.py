"""generate_data.py

The data includes:

Random integers between 1 and 100 in columns 'A' and 'E'
Random choice of letters in column 'B'
Random floats from a normal distribution in column 'C'
Random choice of 1, 2, 3 in column 'D'
Random choice of fruits in column 'F'
Random floats from a uniform distribution in column 'G'
Random choice of 'x', 'y', 'z' in column 'H'
Some missing values have been introduced in columns 'C' and 'G'.
"""

import numpy as np
import pandas as pd

# Number of data points
n = 100

# Generating random data
data = {
    "A": np.random.randint(1, 100, n),  # Random integers between 1 and 100
    "B": np.random.choice(list("abcdefghij"), n),  # Random choice of letters
    "C": np.random.normal(0, 1, n),  # Random floats from a normal distribution
    "D": np.random.choice([1, 2, 3], n),  # Random choice of 1, 2, 3
    "E": np.random.randint(1, 100, n),  # Random integers between 1 and 100
    "F": np.random.choice(
        ["apple", "banana", "cherry", "date", "elderberry", "fig"], n
    ),  # Random choice of fruits
    "G": np.random.uniform(1, 5, n),  # Random floats from a uniform distribution
    "H": np.random.choice(["x", "y", "z"], n),  # Random choice of 'x', 'y', 'z'
}

# Converting to a DataFrame
df = pd.DataFrame(data)

# Introducing some missing values in columns 'C' and 'G'
df.loc[np.random.choice(df.index, size=int(0.1 * n)), "C"] = np.nan
df.loc[np.random.choice(df.index, size=int(0.1 * n)), "G"] = np.nan

# Saving the DataFrame to a CSV file
df.to_csv("./data/test_random.csv", index=False)
