def heightChecker(heights):
    expected = []
    count = 0
    for i in range(len(heights)):
        expected.append(heights[i])
    expected.sort()
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count

heightChecker([1,2,3,5,4,6,1])