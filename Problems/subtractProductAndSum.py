def subtractProductAndSum(n):
    num = str(n)
    nArray = []
    for i in num:
        nArray.append(i)
    j = len(nArray)
    productn = 1
    sumn = 0
    for i in range(0, j):
        productn = productn * int(nArray[i])
    for i in range(0, j):
        sumn = sumn + int(nArray[i])
    diff = productn - sumn
    return diff

subtractProductAndSum(78691)


# Runtime: 32 ms, faster than 57.42% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 14.1 MB, less than 88.62% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.