import itertools

n = int(input())
m = int(input())

replc = len(list(itertools.combinations(range(n), m)))

print(f"\nTotal combinations (C({n},{m})) without replacement: {replc}")