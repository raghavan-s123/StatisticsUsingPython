
print("BuyBloom Probability Calculator")

order_ship = int(input("Enter total number of orders shipped: "))
order_ret = int(input("Enter number of orders returned: "))
notret_prob = (order_ship - order_ret) / order_ship
print(f"Probability a randomly selected order was NOT returned: {notret_prob:.4f}")

print()
deli_part = int(input("Enter total number of delivery partners: "))
delay_part = int(input("Enter number of delayed partners: "))

time_part = deli_part - delay_part
prob_of_1 = time_part / deli_part
prob_of_2 = (time_part - 1) / (deli_part - 1)
time_total_prob = prob_of_1 * prob_of_2

print(f"Probability both randomly chosen partners are on time: {time_total_prob:.4f}")

print()
dis_prob = float(input("Enter probability of a product getting a discount (0 to 1): "))
num_dis = int(input("Enter number of products chosen: "))
total_dis_prob = pow(dis_prob, num_dis)
print(f"Probability all {num_dis} randomly chosen products get discount: {total_dis_prob:.4f}")

print()
no_days = int(input("Enter total number of days in the period (e.g., 7): "))
days_deal = int(input("Enter number of days with deals (out of 7): "))
deal_prob = days_deal / no_days
print(f"Probability of finding a deal on a random day: {deal_prob:.4f}")