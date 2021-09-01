def balancedStringSplit(s):
    balance = 0
    balanceCount = 0
    for i in s:
        if i == "R":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            balanceCount += 1
    return balanceCount

balancedStringSplit("LLLLRRRR")


# Runtime: 28 ms, faster than 84.25% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14.3 MB, less than 10.84% of Python3 online submissions for Split a String in Balanced Strings.