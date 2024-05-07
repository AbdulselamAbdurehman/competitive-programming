class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        shot = points[0]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] > shot[1]:
                count += 1
                shot = points[i]
            shot[1] = min(points[i][1], shot[1])
        return count
