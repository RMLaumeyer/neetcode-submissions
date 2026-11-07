class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(points):
            return ((points[0] ** 2) + (points[1] **2)) ** 0.5

        start = 0
        end = len(points) - 1

        while start <= end:
            pivot = dist(points[end])
            j = start

            for i in range(start, end):
                if dist(points[i]) < pivot:
                    temp = points[i]
                    points[i] = points[j]
                    points[j] = temp
                    j += 1

            temp = points[j]
            points[j] = points[end]
            points[end] = temp

            if j == k-1:
                break
            elif j < k -1:
                start = j + 1
            else:
                end = j - 1

        return points[:k]

