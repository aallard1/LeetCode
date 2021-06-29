def duplicateZeros(arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                i += 1
                arr.pop()
            i += 1

duplicateZeros([1,0,2,3,0,4,5,0])