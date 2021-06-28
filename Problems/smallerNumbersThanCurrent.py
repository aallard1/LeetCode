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