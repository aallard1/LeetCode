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