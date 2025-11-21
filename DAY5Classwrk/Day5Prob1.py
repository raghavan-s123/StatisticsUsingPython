import pandas as pd
import sys
import os

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

print("Loan Data Analysis Started.")
print()

print("First 5 Rows")
print(df.head())
print("Column Names")
print(list(df.columns))
print("Dataset Shape")

print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("Column Data Types and Non-Null Counts")

for col in df.columns:
    non_null = df[col].notnull().sum()
    dtype = df[col].dtype
    print(f"{col:20} Non-Null: {non_null}   Type: {dtype}")

print("Summary Statistics")
print(df.describe())
print("Value Counts for 'purpose'")
print(df['purpose'].value_counts())
print("Value Counts for 'credit.policy'")
print(df['credit.policy'].value_counts())
print("Value Counts for 'not.fully.paid'")
print(df['not.fully.paid'].value_counts())