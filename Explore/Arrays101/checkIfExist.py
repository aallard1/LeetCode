def checkIfExist(arr):
    i = 0
    for j in arr:
        if j != 0 and j * 2 in arr:
            return True
        elif j == 0:
            i += 1
    return True if i > 1 else False
    
    # m = 0   
    # j = 0
    # while j < len(arr):
    #     for i in range(len(arr)):
    #         m = arr[i]
    #         n = m * 2
    #         if n in arr:
    #             return True
    #         else:
    #             return False
    #     j += 1

checkIfExist([7,1,14,11])