import random

population = list(range(1, 101))

sample_size = 10

sample = random.sample(population, sample_size)
print("Sample:", sample)