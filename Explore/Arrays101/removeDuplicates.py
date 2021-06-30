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

removeDuplicates([0,0,1,1,1,2,2,3,3,4])