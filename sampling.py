import math

mean = 170
std = 10
sample_size = 50



sampling_std = std / math.sqrt(sample_size)

print(f"Mean : {mean}")
print(f"Standard deviation: {sampling_std:.3f}")


prop = 0.30
sample_size = 200

std_error = math.sqrt(prop * (1 - prop) / sample_size)
print(f"Standard error: {std_error:.3f}")