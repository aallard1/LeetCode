nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# print(nums1[:m:])
def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(n + m):
            if j == n:
                break
            if nums2[j] <= nums1[i] or (i - j) >= m:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1

        # j = 0
        # while j < len(nums1):
        #     for i in len(nums2):
        #         if nums1[i] == 0:
        #             nums1.insert(j, nums2[i])
        #             j += 1
        #             nums1.pop()
        #         j += 1

merge([1,2,3,0,0,0], 3, [2,5,6], 3)