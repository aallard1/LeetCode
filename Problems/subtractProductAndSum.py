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