def decompressRLElist(nums):
    newNums = []
    for i in range(0, len(nums), 2):
        value = nums[i + 1]
        newNums += nums[i] * [value]
    return newNums

decompressRLElist([1,2,3,4])