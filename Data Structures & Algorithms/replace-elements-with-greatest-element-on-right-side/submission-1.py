class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        localmax = -1

        for i in range(len(arr)-1, -1,-1):
            temp = arr[i]
            arr[i] = localmax
            localmax = max(localmax, temp)

        return arr