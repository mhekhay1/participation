import random

# create a list of 100 random integers from 1 to 10 (inclusive)
nums = [random.randint(1, 10) for _ in range(100)]

# print the sum of the list
print(sum(nums))

# print the average of the list
print(sum(nums) / len(nums))