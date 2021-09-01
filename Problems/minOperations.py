def minOperations(boxes):
    boxCount = []
    for i in range(0, len(boxes)):
        if boxes[i] == "1":
            boxCount.append(i)
    answer = []
    for i in range(0, len(boxes)):
        t = 0
        for j in range(0, len(boxCount)):
            t += abs(boxCount[j]-i)
        answer.append(t)
    return answer

minOperations("110")


# Runtime: 4376 ms, faster than 33.88% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
# Memory Usage: 14.4 MB, less than 91.36% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.

    # stk = []
    # for i in range(0, len(boxes)):
    #     if boxes[i] =="1":
    #         stk.append(i)
    # ans = []
    # for i in range(0, len(boxes)):
    #     t = 0
    #     for j in range(0, len(stk)):
    #         t += abs(stk[j]-i)
    #     ans.append(t)
    # return ans

# Did not work