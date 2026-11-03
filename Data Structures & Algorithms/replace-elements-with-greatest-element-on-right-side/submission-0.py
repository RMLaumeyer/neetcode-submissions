class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        localmax = float('inf')

        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            localmax = 0
            for j in range(i+1, len(arr)):
                if arr[j] > localmax:
                    localmax = arr[j]
            arr[i] = localmax