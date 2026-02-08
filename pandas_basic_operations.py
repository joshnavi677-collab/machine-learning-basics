# Basic Pandas Operations for AIML

import pandas as pd

# Create a simple DataFrame
data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)

# Basic information
print("\nShape of DataFrame:", df.shape)
print("Column names:", df.columns)

# Statistical summary
print("\nSummary statistics:")
print(df.describe())
