import pandas as pd
import os
import sys
from scipy.stats import skew, kurtosis

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

print(f"File loaded successfully: {file}")
print(f"Data shape: {df.shape}")
print("Preview of Loaded Data:")
print(df.head())


def simple():
    print("Simple Random Sampling (50 students):")
    simple = df.sample(n=50, random_state=42)
    print(simple.head().reset_index(drop=True))
    
    print("Summary Statistics of the Population data")
    heigh = df['Height_cm']
    print(round(heigh.describe(), 1))
    med = heigh.median()
    mod = heigh.mode()
    ske = skew(heigh)
    kurt = kurtosis(heigh)
    
    print(f"median: {med} mode: {mod[0]}")
    print(f"skewness: {round(ske, 3)} kurtosis: {round(kurt, 3)}")
    
    print("Summary Statistics of the Sample data")
    ran_heigh = simple['Height_cm']
    print(round(ran_heigh.describe(), 1))
    med = ran_heigh.median()
    mod = ran_heigh.mode()
    ske = skew(ran_heigh)
    kurt = kurtosis(ran_heigh)
    
    print(f"median: {med} mode: {mod[0]}")
    print(f"skewness: {round(ske, 3)} kurtosis: {round(kurt, 3)}")


if __name__ == "__main__":
    simple()
