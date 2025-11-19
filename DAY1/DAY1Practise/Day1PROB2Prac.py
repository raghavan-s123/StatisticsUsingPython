
prodA = list(map(int, input("Enter counts for Product A: ").split(',')))
prodB = list(map(int, input("Enter counts for Product B: ").split(',')))
prodC = list(map(int, input("Enter counts for Product C: ").split(',')))
prodD = list(map(int, input("Enter counts for Product D: ").split(',')))

a_total = sum(prodA)
b_total = sum(prodB)
c_total = sum(prodC)
d_total = sum(prodD)

total = a_total + b_total + c_total + d_total

prob_a_25 = prodA[0] / total

print()
print(f"Probability of Product A by someone aged < 25: {prob_a_25:.4f}")

prob_c_25_40 = prodC[1] / c_total
print(f"Probability of age 25-40 given Product C purchase: {prob_c_25_40:.4f}")

total_41_60 = prodA[2] + prodB[2] + prodC[2] + prodD[2]
prob_41_60 = total_41_60 / total
print(f"Overall probability of buyer from 41-60 age group: {prob_41_60:.4f}")

print()

b_and_60 = prodB[3] / total
print(f"P(Product B and Age 60+): {b_and_60:.4f}")

b_prob = b_total / total
print(f"    P(Product B): {b_prob:.4f}")

total_60 = prodA[3] + prodB[3] + prodC[3] + prodD[3]
prob_60 = total_60 / total
print(f"    P(Age 60+): {prob_60:.4f}")

b_mul_60 = b_prob * prob_60
print(f"    P(Product B) * P(Age 60+): {b_mul_60:.4f}")

if abs(b_mul_60 - b_and_60) < 1e-9:
    print("Conclusion: Product B purchases and Age 60+ are INDEPENDENT.")
else:
    print("Conclusion: Product B purchases and Age 60+ are DEPENDENT.")
# print("Conclusion: Product B purchases and Age 60+ are DEPENDENT.")