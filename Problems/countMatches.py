def countMatches(items, ruleKey, ruleValue):
    # newList = []
    countMatches = 0
    for i in items:
        # if ruleKey and ruleValue in i: This did not work for all test cases
        if ruleKey == "type" and i[0] == ruleValue or \
            ruleKey == "color" and i[1] == ruleValue or \
            ruleKey == "name" and i[2] == ruleValue:
            # newList.append(i)
            countMatches +=1
    return countMatches

countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone")


# Runtime: 381 ms, faster than 6.37% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.5 MB, less than 89.13% of Python3 online submissions for Count Items Matching a Rule.