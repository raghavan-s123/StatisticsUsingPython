import pandas as pd
import os
import sys
import numpy as np
from scipy.stats import norm

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))


north = df[df['Zone'] == 'North']['Delivery_Time_Hours']
south = df[df['Zone'] == 'South']['Delivery_Time_Hours']

n_sample = min(50, len(north), len(south)) #NO OF SAMPLES = 50, GIVEN IN PROBLEM ITSELF

north_sample = north.sample(n=n_sample, random_state=42)
south_sample = south.sample(n=n_sample, random_state=42)

mean_diff = north_sample.mean() - south_sample.mean()

z_val = mean_diff / (1.41 * np.sqrt(2 / n_sample)) #STD  = 1.41 GIVEN IN PROBLEM ITSELF

p_val = 2 * (1 - norm.cdf(abs(z_val)))

print(f"Sample Size per Group: {n_sample}")
print(f"Mean Delivery Time (North): {north_sample.mean():.2f}")
print(f"Mean Delivery Time (South): {south_sample.mean():.2f}")
print(f"Z-Statistic: {z_val:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val > 0.05:
    print("Fail to reject the null hypothesis: No significant difference in delivery times.")
else:
    print("Reject the null hypothesis: There IS a significant difference in delivery times.")