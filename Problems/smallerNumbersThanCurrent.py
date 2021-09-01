def smallerNumbersThanCurrent(nums):
    count = 0
    numsDict = {}
    for i in nums:
        if i in numsDict:
            numsDict[i] += 1
        else:
            numsDict[i] = 1
    for i in range(len(nums)):
            count = 0
            for key, val in numsDict.items():
                if key < nums[i]:
                    count += val
            nums[i] = count
    return nums

smallerNumbersThanCurrent([6,5,4,8])


# Runtime: 224 ms, faster than 44.24% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14.3 MB, less than 47.97% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.