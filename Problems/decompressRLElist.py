def decompressRLElist(nums):
    newNums = []
    for i in range(0, len(nums), 2):
        value = nums[i + 1]
        newNums += nums[i] * [value]
    return newNums

decompressRLElist([1,2,3,4])


# Runtime: 110 ms, faster than 5.17% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14.9 MB, less than 26.13% of Python3 online submissions for Decompress Run-Length Encoded List.