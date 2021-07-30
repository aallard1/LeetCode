def thirdMax(nums):
    x = set(nums)
    y = list(x)
    y.sort()
    if len(y) < 3:
        return max(y)
    else:
        return y[-3]

thirdMax([3,2,1])