import pandas as pd
import os
import sys
import numpy as np
from scipy.stats import chi2_contingency

def get_weektype(d):
    return 'Weekend' if d in [1, 7] else "Weekday"

file = input()
df = pd.read_csv(os.path.join(sys.path[0], file))

df['Date'] = pd.to_datetime(
        df['Date'],
        errors='coerce'
    )

df['WeekType'] = df['Day.Of.Week'].apply(get_weektype)
df['Year'] = df['Date'].dt.year

table = pd.pivot_table(
        df,
        index='Year',
        columns='WeekType',
        values='Page.Loads',
        aggfunc='sum',
        fill_value=0
    )
print("Contingency Table:")
print(table)

chi_val, p_val, dof, expected = chi2_contingency(table)

print()
print(f"Chi-Square Statistic: {chi_val:.2f}")
print(f"p-value: {p_val:.4f}")
print()

if p_val > 0.01:
    print("Fail to Reject H0: No significant difference in Page Load distributions across years.")