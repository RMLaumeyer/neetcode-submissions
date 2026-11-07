class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                break

        if left > right:
            return False

        left = 0
        right = len(matrix[mid]) - 1

        while left <= right:
            nmid = (left + right) // 2

            if matrix[mid][nmid] < target:
                left = nmid + 1
            elif matrix[mid][nmid] > target:
                right = nmid - 1
            else:
                return True

        return False