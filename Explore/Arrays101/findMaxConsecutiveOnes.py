# def findMaxConsecutiveOnes(nums):
#     count = 0
#     newCount = 0
#     if 0 in nums:
#         for i in range(len(nums)):
#             if len(nums) == 2:
#                 if nums[i] == 1:
#                     count += 1
#                     if count >= 1:
#                         if count > newCount:
#                             newCount = count
#                             count = 0
#                         elif count == newCount:
#                             newCount += count
#                             count = 0
#                         else:
#                             count = 0
#                 if nums[i] == 0:
#                     count = 0
#             if len(nums) <= 3:
#                 if nums[i] == 1:
#                     count += 1
#                     if count >= 1:
#                         if count > newCount:
#                             newCount = count
#                             count = 0
#                 if nums[i] == 0:
#                     count = 0
#             elif len(nums) >= 3:
#                 if nums[i] == 1:
#                     count += 1
#                     if count >= 2:
#                         if count > newCount:
#                             newCount = count
#                             count = 0
#                 elif nums[i] == 0:
#                     count = 0
#     else:
#         for i in range(len(nums)):
#             if len(nums) == 1 and nums[i] == 1:
#                 newCount = 1
#                 return newCount
#         temp = 0
#         for i in range(0, len(nums)):
#             temp += nums[i]
#             nums[i] = temp                
#         return nums[i]
#     return newCount

# Above solution would not work

def findMaxConsecutiveOnes(nums):
    count = 0
    maxNum = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        if nums[i] == 0 or i == len(nums)-1:
            if maxNum < count:
                maxNum = count
            count = 0
    return maxNum
            