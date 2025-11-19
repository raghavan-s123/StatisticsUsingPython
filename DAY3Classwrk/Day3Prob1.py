import math
from scipy.stats import norm

x = float(input())
mu = float(input())
sigma = float(input())
n = int(input())
type_test = input()
alpha_in = input()

alpha = float(alpha_in) if alpha_in else 0.05

z_stat = (x - mu) / (sigma / math.sqrt(n)) # ONE SAMPLE TEST Z FORMULA

print(f"Z-statistic: {round(z_stat, 4)}")

if type_test == 'greater':
    p_stat = 1 - norm.cdf(z_stat)
elif type_test == 'less':
    p_stat = norm.cdf(z_stat)
else:
    p_stat = 2 * (1 - norm.cdf(abs(z_stat)))
    
print(f"P-value: {round(p_stat, 4)}")

if p_stat < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")

    
