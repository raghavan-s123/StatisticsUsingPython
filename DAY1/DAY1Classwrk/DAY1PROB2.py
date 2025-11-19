import pandas as pd

age_group = ["18–25", "26–40", "40+"]

coffee_type = ["Latte", "Black Coffee"]

total_customer = 0

data = {coffee: [] for coffee in coffee_type}
for age in age_group:
    print(f"\nAge group: {age}")
    for coffee in coffee_type:
        count = int(input(f"Number of customers who prefer {coffee}: "))
        total_customer += count
        data[coffee].append(count)

df = pd.DataFrame(data, index=age_group)
print("\nData Summary:")
print(df)

age40_black = df.loc['40+', 'Black Coffee']
join_prob = age40_black / total_customer

print()
print(f"Joint Probability P(Age 40+ and Black Coffee): {join_prob:.4f}")


age40 = df.loc['40+'].sum()
join_prob = age40_black / age40  

print(f"Conditional Probability P(Black Coffee | Age 40+): {join_prob:.4f}")
print()

black = df['Black Coffee'].sum()
over_prob = black / total_customer
print(f"Overall Probability P(Black Coffee): {over_prob:.4f}")
print(f"Conditional Probability P(Black Coffee | Age 40+): {join_prob:.4f}")

if abs(join_prob - over_prob) < 1e-4:
    print("Age (being 40 or older) does NOT influence preference for Black Coffee.")
else:
    print("Age (being 40 or older) influences preference for Black Coffee.")
# print("Age (being 40 or older) influences preference for Black Coffee.")

