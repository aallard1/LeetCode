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
minOperations("110")