def replaceElements(arr):
    num = len(arr) - 1
    rightMax = arr[num]
    for i in range(num - 1, -1, -1):
        c = arr[i]
        arr[i] = rightMax
        rightMax = max(rightMax, c)
    arr[-1] = -1
    return arr

replaceElements([17,18,5,4,6,1])