import numpy as np
from statsmodels.stats.weightstats import ztest

mean_boys = float(input())
std_boys = float(input())
n_boys = int(input())

mean_girl = float(input())
std_girl = float(input())
n_girl = int(input())

alpha=0.05
np.random.seed(42)

boys_height = np.random.normal(loc=mean_boys, scale=std_boys, size=n_boys)
girls_height = np.random.normal(loc=mean_girl, scale=std_girl, size=n_girl)

z_stat, p_value = ztest(boys_height, girls_height, alternative='larger')


print("Two-Sample Z-Test Result (Boys > Girls)")
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: Boys are significantly taller than girls.")
else:
    print("Fail to reject the null hypothesis: No significant evidence that boys are taller than girls.")