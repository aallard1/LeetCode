def shuffle(nums, n):
    newNumsArr = []
    for i in range(n):
        newNumsArr.append(nums[i])
        newNumsArr.append(nums[i+n])
    return newNumsArr

print(shuffle([2,5,1,3,4,7], 3))