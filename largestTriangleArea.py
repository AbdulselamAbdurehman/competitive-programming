class Solution:
    def largestTriangleArea(self, pts: List[List[int]]) -> float:
        largest = 0
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                for k in range(j+1, len(pts)):
                    area = abs(1/2*(pts[i][0]*(pts[j][1]-pts[k][1]) + \
                     pts[j][0]*(pts[k][1] - pts[i][1]) + \
                     pts[k][0]*(pts[i][1] - pts[j][1])))
                    if area > largest:
                        largest = area
        return largest
