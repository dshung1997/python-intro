nums = [1, 4, 2, 5, 6, 10, 3]
print(sorted(nums, reverse=True))

nums = [1, 4, 3]
print(sorted(nums, reverse=True))

nums = [1, 2]
print(sorted(nums, reverse=True)[min(2, len(nums) - 1)])

nums = [1]
print(sorted(nums, reverse=True))
