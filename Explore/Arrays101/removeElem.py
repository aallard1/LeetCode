def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

removeElement([3,4,5,6,3,3], 3)