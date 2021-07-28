def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    x = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[x] = nums[i]
            x += 1
    while x < len(nums):
        nums[x] = 0
        x += 1

moveZeroes([0,1,0,2,4,5,9,0])