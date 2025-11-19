import pandas as pd
import os
import sys
from scipy.stats import ttest_ind

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

east = df[df['Zone'] == 'East']['Delivery_Time_Hours']
west = df[df['Zone'] == 'West']['Delivery_Time_Hours']

east_mean = east.mean()
west_mean = west.mean()

print(f"East Mean: {east_mean:.2f}")
print(f"West Mean: {west_mean:.2f}")


t_val, p_val = ttest_ind(east, west, equal_var=True)
print(f"T-statistic: {t_val:.4f}")
print(f"P-value: {p_val:.4f}")

if p_val > 0.05:
    print("Fail to reject the null hypothesis: No significant difference in delivery times between East and West.")
else:
    print("Reject the null hypothesis: There IS a significant difference in delivery times between East and West.")
    