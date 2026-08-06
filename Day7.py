# 1. Two Sum Problem
def two_sum(nums, target):
    d = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in d:
            return [d[complement], i]

        d[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

# 2. Kadane's Algorithm (Maximum Subarray Sum)
def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(arr))
