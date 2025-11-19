import random
import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split

file = input()
print(f"File loaded successfully: {file}")

df = pd.read_csv(os.path.join(sys.path[0], file))
print(f"Data shape: {df.shape}")
print("Preview of Loaded Data:")
print(df.head())

sample_size = 50

def simple():
    print("Simple Random Sampling (50 students):")
    if sample_size > len(df):
        print(f"Not enough rows to sample 50 rows. Total rows: {len(df)}")
    else:   
        sample = df.sample(n=sample_size, random_state=42)
        print(sample.head())
        
def stratified():
    try:
        print("Stratified Sampling (by Gender):")
        stratify_by='Gender'
        
        train, test = train_test_split(
            df,
            test_size = 0.2,
            stratify=df[stratify_by],
            random_state = 42
        )
        print(train.head())
    except Exception:
        print("Stratified sampling failed: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.")
    
def systemic():
    print("Systematic Sampling (every 10th student):")
    systematic_sample = df.iloc[::10]
    print(systematic_sample.head())
    
if __name__ == "__main__":
    simple()
    stratified()
    systemic()