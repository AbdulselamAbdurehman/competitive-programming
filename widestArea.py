class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_cord = [cord[0] for cord in points]
        x_cord.sort()
        optimum = 0
        for i in range(1, len(x_cord)):
            curr = x_cord[i] - x_cord[i-1]
            optimum = max(curr, optimum)
        return optimum
