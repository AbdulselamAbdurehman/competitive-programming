class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = [[0]*n for _ in range(m)]
        for j in range(n-1, -1, -1):
            for i in range(m):
                if j == n-1:
                    result[i][j] = 1
                else:
                    best = 0
                    if grid[i][j] < grid[i][j+1]:
                        best = max(best, result[i][j+1])
                    if i > 0 and grid[i][j] < grid[i-1][j+1]:
                        best = max(best, result[i-1][j+1])
                    if i < m-1 and grid[i][j] < grid[i+1][j+1]:
                        best = max(best, result[i+1][j+1])
                    result[i][j] = best + 1
        return max([result[i][0] for i in range(m)]) - 1