def numIdenticalPairs(nums):
    count = 0
    pairs = {}
    for i in nums:
        if i not in pairs:
            pairs[i] = 0
        else:
            pairs[i] += 1
    for i, j in pairs.items():
        count += (j + 1) * j / 2
    return int(count)

numIdenticalPairs([1,2,3,1,1,3])