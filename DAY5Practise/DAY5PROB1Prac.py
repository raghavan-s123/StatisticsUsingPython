import pandas as pd
import os
import sys

file = input()
print("Enter the CSV file name (e.g., income_data.csv): First 5 Rows:")
df = pd.read_csv(os.path.join(sys.path[0], file))
df.replace('?', 'Unknown', inplace=True)
print(df.head())
print()

print("Column Names:")
print(list(df.columns))

print()
print("Dataset Shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print()
print("Column Data Types and Non-Null Counts:")
for col in df.columns:
    null_sum = df[col].notnull().sum()
    dtype = df[col].dtype
    print(f"{col:25} Non-Null: {null_sum}     Type: {dtype}")
print()

print("Summary Statistics (Numerical Columns):")
print(df.describe())

print()
print("Categorical Columns and Value Counts:")
print()

print("Column: WorkClass")
print(df['WorkClass'].value_counts())
print()

print("Column: Education")
print(df['Education'].value_counts())
print()

print("Column: Marital_Status")
print(df['Marital_Status'].value_counts())
print()

print("Column: Occupation")
print(df['Occupation'].value_counts())
print()

print("Column: Relationship")
print(df['Relationship'].value_counts())
print()

print("Column: Gender")
print(df['Gender'].value_counts())
print()

print("Column: Native_Country")
print(df['Native_Country'].value_counts())
print()

print("Column: Income_Bracket")
print(df['Income_Bracket'].value_counts())
print()

print("Gender Distribution:")
print(df['Gender'].value_counts())
print()