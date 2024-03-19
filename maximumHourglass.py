class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if 1 <= i < m-1 and 1 <= j < n-1:
                    hourglass = grid[i][j] + sum(grid[i-1][j-1:j+2]) + sum(grid[i+1][j-1:j+2])
                    maximum = max(hourglass, maximum)
        return maximum
