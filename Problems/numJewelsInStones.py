def numJewelsInStones(jewels, stones):
    count = 0
    for i in range(0, len(stones)):
        if stones[i] in jewels:
            count += 1
    return count

numJewelsInStones("aA", "aAAbbbb")


# Runtime: 57 ms, faster than 5.51% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.2 MB, less than 46.25% of Python3 online submissions for Jewels and Stones.