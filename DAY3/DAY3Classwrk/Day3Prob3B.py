import numpy as np
from scipy.stats import ttest_rel

mean_before = float(input())
std_before = float(input())
mean_after = float(input())
std_after = float(input())
n = int(input())

np.random.seed(42)
ratings_before = np.random.normal(mean_before, std_before, n)

effect = mean_after - mean_before
ratings_after = ratings_before + effect + np.random.normal(0, 0.1, n)

t_statistic, p_value = ttest_rel(ratings_after, ratings_before)

print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in fit ratings before and after the intervention.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in fit ratings before and after the intervention.")
