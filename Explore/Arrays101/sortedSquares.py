def sortedSquares(nums):
    newNums = []
    for i in nums:
        square = i ** 2
        newNums.append(square)
    newNums.sort()
    return newNums

sortedSquares([-7,-3,2,3,11])