import pandas as pd
import os
import sys
import math
from scipy.stats import norm

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))
mean = float(input())
std = float(input())

print(f"File loaded successfully: {file}")
print(f"Data shape: {df.shape}")

del_time = df['Delivery_Time_Hours']
n = len(del_time)
sample_mean = del_time.mean()

z_val = (sample_mean - mean) / (std / math.sqrt(n))
p_val = 2 * (1 - norm.cdf(abs(z_val))) #Two-Tailed

print()
print(f"Z-statistic: {z_val:.4f}")
print(f"P-value: {p_val:.4f}")

if p_val > 0.05:
    print("Fail to reject the null hypothesis. There is not enough evidence to suggest the delivery time differs from the hypothesized mean.")
else:
    print("Reject the null hypothesis. There is enough evidence to suggest the delivery time differs from the hypothesized mean.")