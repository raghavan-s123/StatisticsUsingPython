# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# -----------------------------
# Step 1: Load population data from Excel
# -----------------------------
df = pd.read_excel('ML374_S2_Height_Weight_Data_Concept.xlsx')  # replace with your Excel file
population_heights = df['Height_cm']
print("First few rows of population heights:")
print(population_heights.head())

# -----------------------------
# Step 2: CLT parameters
# -----------------------------
sample_size = 50           # size of each sample
num_samples = 450          # number of samples to draw
random_seed = 42           # fixed seed for reproducibility

# -----------------------------
# Step 3: Draw samples and compute means (with fixed seed)
# -----------------------------
sample_means = []

rng = np.random.default_rng(random_seed)  # NumPy random generator for reproducibility

for _ in range(num_samples):
    # sample with fixed random generator
    sample = population_heights.sample(n=sample_size, random_state=rng.integers(0, 100000))
    sample_mean = sample.mean()
    sample_means.append(sample_mean)

sample_means = np.array(sample_means)

# -----------------------------
# Step 4: Plot histogram (Count vs Sample Mean) with KDE
# -----------------------------
plt.figure(figsize=(12,6))
sns.histplot(sample_means, bins=30, kde=True, color='teal')
plt.title(f"CLT: Count vs Sample Mean Height (n={sample_size}, {num_samples} samples)")
plt.xlabel("Sample Mean of Height_cm")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Step 5: Print summary statistics
# -----------------------------
print(f"Population mean: {population_heights.mean():.2f}")
print(f"Population std deviation: {population_heights.std():.2f}")
print(f"Sampling distribution mean: {sample_means.mean():.2f}")
print(f"Sampling distribution std deviation (Standard Error): {sample_means.std():.2f}")
