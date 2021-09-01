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


# Runtime: 56 ms, faster than 6.27% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.3 MB, less than 10.64% of Python3 online submissions for Number of Good Pairs.