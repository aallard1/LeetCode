def removeDuplicates(nums):
    i = 0
    while i < len(nums):
        if len(nums) == 1:
            break
        elif nums[i] == nums[i - 1]:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)

# Runtime: 263 ms, faster than 5.59% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.7 MB, less than 46.28% of Python3 online submissions for Remove Duplicates from Sorted Array.

    # uniqueNum = 0
    # for i in range(len(nums)):
    #     if i == 0 or nums[i] != nums[i + 1]:
    #         uniqueNum += 1
    # for i in range(len(nums)):
    #     if i == 0 or nums[i] != nums[i + 1]:

# Wrong Answer