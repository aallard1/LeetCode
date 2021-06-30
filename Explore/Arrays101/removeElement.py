def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(val)
        else:
            i += 1
    return len(nums)

removeElement([0,1,2,3,4,4,4,4], 4)
