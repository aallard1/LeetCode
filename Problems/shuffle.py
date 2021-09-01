def shuffle(nums, n):
    newNumsArr = []
    for i in range(n):
        newNumsArr.append(nums[i])
        newNumsArr.append(nums[i+n])
    return newNumsArr

print(shuffle([2,5,1,3,4,7], 3))


# Runtime: 106 ms, faster than 5.12% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.5 MB, less than 49.67% of Python3 online submissions for Shuffle the Array.