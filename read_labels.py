import pandas as pd

# load train labels
df = pd.read_csv("Dataset/xview3/train.csv")

# show first few rows
print(df.head())

# show all column names
print("\nColumns:")
print(df.columns)