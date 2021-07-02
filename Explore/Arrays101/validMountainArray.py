def validMountainArray(arr):
    isMountain = False  
    if len(arr) < 3 or arr[0] > arr[1]:
        return False
    for i in range(len(arr)-1):
        if not isMountain and not arr[i] < arr[i+1]:
            isMountain = True
        if isMountain and not (arr[i] > arr[i+1]):
            return False
        if not isMountain and i == len(arr)-2:
            return False
    return True
    
    # isMountain = False
    # if len(arr) < 3 or arr[0] > arr[1]:
    #     return False
    # elif len(arr) <= 3 and arr[1] == arr[2]:
    #     return False
    # for i in range(len(arr)-1):
    #     if not isMountain and not arr[i] < arr[i+1]:
    #         isMountain = True
    #     elif isMountain and not (arr[i] > arr[i+1]):
    #         return False
    #     elif not isMountain and i == len(arr)-2:
    #         return False
    #     else:
    #         return True
    # return True