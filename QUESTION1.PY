import numpy as np

arr = np.arange(10, 101, 10)

first_three = arr[:3]
last_two = arr[-2:]
third_to_seventh = arr[2:7]
reversed_arr = arr[::-1]
greater_than_25 = arr[arr > 25]

print("First three:", first_three)
print("Last two:", last_two)
print("3rd to 7th:", third_to_seventh)
print("Reversed:", reversed_arr)
print("Greater than 25:", greater_than_25)
