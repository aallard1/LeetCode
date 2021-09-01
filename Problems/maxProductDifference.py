def maxProductDifference(nums):
    nums.sort()
    a = int(nums[-1])
    b = int(nums[-2])
    c = int(nums[0])
    d = int(nums[[1]])
    productDiff = (a * b) - (c * d)
    return productDiff

maxProductDifference([5,6,2,7,4])

# Runtime: 172 ms, faster than 38.27% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
# Memory Usage: 15.4 MB, less than 46.80% of Python3 online submissions for Maximum Product Difference Between Two Pairs.