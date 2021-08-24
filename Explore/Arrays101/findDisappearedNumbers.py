def findDisappearedNumbers(nums):
    mySet = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in mySet]