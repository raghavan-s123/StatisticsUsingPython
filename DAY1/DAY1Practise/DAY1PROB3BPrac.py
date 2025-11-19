import itertools


n = int(input())
m = int(input())

total = len(list(itertools.permutations(range(n), m)))

print(f"Total permutations (P({n},{m})) without replacement: {total}")