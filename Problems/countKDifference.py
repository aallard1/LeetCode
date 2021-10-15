def countKDifference(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = nums[i] - nums[j]
            if diff == k or diff == -k:
                count += 1
    return count

countKDifference([1,2,2,1], 1)

# Runtime: 275 ms, faster than 28.36% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
# Memory Usage: 14.1 MB, less than 79.47% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.

def countKDifference(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                count += 1
    return count

# Runtime: 321 ms, faster than 17.60% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
# Memory Usage: 14.4 MB, less than 20.76% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.