import math

print("PIN Permutation Generator")

print("Enter digits to use for PIN separated by commas (e.g., 0,1,2,3,4): Enter the length of the PIN (e.g., 3): ")

arr = list(map(int, input().split(',')))

arr_len = len(arr)
pin_len = int(input())

dupli_permu = pow(arr_len, pin_len)
uni_permu = math.factorial(arr_len) / math.factorial(arr_len - pin_len)
print("PIN Permutations")


print("Total PINs without replacement (unique digits):", int(uni_permu))
print("Total PINs with replacement (digits can repeat):", dupli_permu)

