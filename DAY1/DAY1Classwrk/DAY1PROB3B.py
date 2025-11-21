import math
import itertools

print("Ice Cream Flavor Combination Calculator")

flav_combi = list(map(str, input("Enter ice cream flavors separated by commas (e.g., Vanilla, Chocolate, etc.): ").split(",")))
n = int(input(f"How many flavors do you want to choose (out of {len(flav_combi)} available)?: "))

print()
total = len(flav_combi)
print("Flavor Combinations")

out_repl = len(list(itertools.combinations(flav_combi, n)))
repl = len(list(itertools.combinations_with_replacement(flav_combi, n)))
print(f"Total combinations without replacement: {out_repl}")
print(f"Total combinations with replacement: {repl}")


