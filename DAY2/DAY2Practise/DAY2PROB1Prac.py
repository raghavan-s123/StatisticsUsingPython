import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split

file = input("Enter the dataset filename (with .csv or .xlsx extension): ")
df = pd.read_csv(os.path.join(sys.path[0], file))

print(f"File loaded successfully: {file}")
print(f"Data shape: {df.shape}")

print()

print("Preview of Loaded Data:")
print(df.head())

def simple():
    sample = df.sample(n=50, random_state=42)
    print()
    print("1.1: Simple Random Sample of 50 deliveries:")
    print(sample.head().reset_index(drop=True))

def stratified():
    print()
    print("1.2: Stratified Sample by Zone (proportional to dataset):")
    largest_zone = df['Zone'].value_counts().idxmax()
    
    sample = df[df['Zone'] == largest_zone].sample(5, random_state=42) #ABSOLUTELY $@#
    print(sample.head().reset_index(drop=True))
    
    

def system():
    print()
    print("1.3: Systematic Sample (every 10th order):")
    systemat = df.iloc[::10]
    print(systemat.head().reset_index(drop=True))
if __name__ == "__main__":
    simple()
    stratified()
    system()