def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

# Runtime: 52 ms, faster than 7.30% of Python3 online submissions for Remove Element.
# Memory Usage: 14.3 MB, less than 48.32% of Python3 online submissions for Remove Element.