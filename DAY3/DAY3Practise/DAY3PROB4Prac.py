from scipy.stats import ttest_rel

before_time = list(map(float, input().split(',')))
after_time = list(map(float, input().split(',')))

print(f"Before optimization times: {before_time}")
print(f"After optimization times: {after_time}")

print()
t_val, p_val = ttest_rel(before_time, after_time)

if t_val > 0:
    p_one_val = 1 - (p_val / 2)
else:
    p_one_val = p_val / 2
    
print(f"T-statistic (two-tailed): {t_val:.4f}")
print(f"P-value (two-tailed): {p_val:.4f}")
print(f"P-value (one-tailed): {p_one_val:.4f}")

if p_one_val > 0.05:
    print("Fail to reject null hypothesis: No significant improvement in delivery time.")
else:
    print("Reject null hypothesis: Delivery time improved after optimization.")