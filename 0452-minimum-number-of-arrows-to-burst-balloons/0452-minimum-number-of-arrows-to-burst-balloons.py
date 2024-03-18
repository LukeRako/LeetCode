class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]
            if prev[1] >= curr[0]:
                res -= 1
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                prev = curr

        return res        