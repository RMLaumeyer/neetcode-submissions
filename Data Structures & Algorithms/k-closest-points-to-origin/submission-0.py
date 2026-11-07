class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []

        for i in range(len(points)):
            dist = ((points[i][0] ** 2) + (points[i][1] **2)) ** 0.5
            l.append((dist, points[i]))

        l.sort()
        result = []

        for i in range(k):
            result.append(l[i][1])



        return result

