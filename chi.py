import numpy as py
from scipy.stats import chi2_contingency
import pandas as pd

data = {"Drink":["coffee", "Orange", "Apple"], "male":[40, 50, 60], "Female":[25, 30, 35]}

df = pd.DataFrame(data)
table = df[['male', 'Female']].values
chi2, p, dof, expected = chi2_contingency(table)
print(f"Chi-squared statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print(expected)