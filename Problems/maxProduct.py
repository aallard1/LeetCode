def maxProduct(self, nums: List[int]) -> int:
    nums.sort() # Sorts the values in nums, ascending order
    maxVal = (nums[-1] - 1) * (nums[-2] - 1)
    return maxVal

maxProduct([3,4,5,2])

# Runtime: 57 ms, faster than 43.93% of Python3 online submissions for Maximum Product of Two Elements in an Array.
# Memory Usage: 14.3 MB, less than 71.31% of Python3 online submissions for Maximum Product of Two Elements in an Array.