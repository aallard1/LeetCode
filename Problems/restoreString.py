def restoreString(s, indices):
    newS = [None] * len(s)
    for i in range(len(s)):
        newS[indices[i]] = s[i]
    return "".join(newS)


# Runtime: 62 ms, faster than 20.12% of Python3 online submissions for Shuffle String.
# Memory Usage: 14.3 MB, less than 21.37% of Python3 online submissions for Shuffle String.