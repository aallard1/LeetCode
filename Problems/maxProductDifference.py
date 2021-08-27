def maxProductDifference(nums):
    nums.sort()
    a = int(nums[-1])
    b = int(nums[-2])
    c = int(nums[0])
    d = int(nums[[1]])
    productDiff = (a * b) - (c * d)
    return productDiff

maxProductDifference([5,6,2,7,4])