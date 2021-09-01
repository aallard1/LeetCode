def runningSum(nums):
        temp = 0
        for i in range(0, len(nums)):
            temp += nums[i]
            nums[i] = temp
            
        return nums


# Runtime: 50 ms, faster than 20.56% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.5 MB, less than 12.02% of Python3 online submissions for Running Sum of 1d Array.