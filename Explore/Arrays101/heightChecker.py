def heightChecker(heights):
    expected = []  
    count = 0                       # will use to count number of times expected and heights don't match
    lenHeight = len(heights)
    for i in range(lenHeight):      # add all heights values to expected
        expected.append(heights[i])
    expected.sort()                 # sorts all values in ascending order 
    for i in range(lenHeight):      # count number of times expected and heights do not match up
        if heights[i] != expected[i]:
            count += 1
    return count                    # gives back the count

heightChecker([1,2,3,5,4,6,1])