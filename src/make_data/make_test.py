import pandas as pd

# Creating a simple DataFrame for testing
data = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': ['a', 'b', 'c', 'd', 'e', 'f'],
    'C': [1.1, 2.2, 3.3, 4.4, None, 6.6],
    'D': [1, 1, 2, 2, 3, 3]  # Duplicates
}

df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
df.to_csv('./data/test.csv', index=False)
