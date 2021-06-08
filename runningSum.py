def runningSum(nums):
        temp = 0
        for i in range(0, len(nums)):
            temp += nums[i]
            nums[i] = temp
            
        return nums