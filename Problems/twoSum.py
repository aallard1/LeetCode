def twoSum(nums, target):
    a = {}

    for i, j in enumerate(nums):
        remainder = target - j
        
        if remainder in a:
            return[i, a[remainder]]
        else:
            a[j] = i
    
    return []

print(twoSum([2,5,5,11], 10))

# Runtime: 60 ms, faster than 75.03% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 54.26% of Python3 online submissions for Two Sum.


# def twoSum(nums, target):
#     potentialnum = []

#     while len(potentialnum) != 2:
#         for i in range(0, len(nums)):
#             if nums[i] < target:
#                 potentialnum.append(i)
#             if len(potentialnum) == 2:
#                 sumnum = nums[potentialnum[0]] + nums[potentialnum[1]]
#                 if sumnum == target:
#                     return potentialnum
#                 elif sumnum < target:
#                     if nums[potentialnum[0]] < nums[potentialnum[1]]:
#                         potentialnum.pop(0)
#                     else:
#                         potentialnum.pop(1)
#                 else:
#                     if nums[potentialnum[0]] > nums[potentialnum[1]]:
#                         potentialnum.pop(1)
#                     else:
#                         potentialnum.pop(0)

# Time Limit Exceeded