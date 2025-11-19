import numpy as np
from scipy.stats import ttest_ind

np.random.seed(42)

male_mean = float(input())
male_std = float(input())
male_no = int(input())

fem_mean = float(input())
fem_std = float(input())
fem_no = int(input())

male_data = np.random.normal(loc=male_mean, scale=male_std, size=male_no)

female_data = np.random.normal(loc=fem_mean, scale=fem_std, size=fem_no)

t_stat, p_value = ttest_ind(male_data, female_data)

print("Two-Sample T-Test Result (Male vs Female Fit Ratings)")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value > 0.05:
    print("Fail to reject the null hypothesis: No significant difference in fit ratings between male and female respondents.")
else:
    print("Reject the null hypothesis: Significant difference in fit ratings between male and female respondents.")