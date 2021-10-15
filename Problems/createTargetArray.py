def createTargetArray(nums, index):
    newNums = []
    for i in range(len(nums)):
        newNums.insert(index[i], nums[i])
    return newNums

createTargetArray([0,1,2,3,4], [0,1,2,2,1])

# Runtime: 36 ms, faster than 60.78% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 14.2 MB, less than 76.87% of Python3 online submissions for Create Target Array in the Given Order.