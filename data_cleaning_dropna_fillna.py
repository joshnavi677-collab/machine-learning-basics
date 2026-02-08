# Data Cleaning using Pandas (dropna & fillna)

import pandas as pd

# Load CSV file
df = pd.read_csv("sample_data.csv")

print("Original Data:")
print(df)

# Drop rows with missing values
df_dropna = df.dropna()
print("\nAfter dropna():")
print(df_dropna)

# Fill missing values
df_fillna = df.fillna({
    "Age": df["Age"].mean(),
    "Marks": df["Marks"].mean()
})

print("\nAfter fillna():")
print(df_fillna)
