def restoreString(s, indices):
    newS = [None] * len(s)
    for i in range(len(s)):
        newS[indices[i]] = s[i]
    return "".join(newS)