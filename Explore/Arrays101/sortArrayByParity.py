def sortArrayByParity(nums):
    newNums = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            newNums.append(nums[i])
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            newNums.append(nums[i])
    return newNums

sortArrayByParity([3,1,2,4])