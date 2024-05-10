class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax, colMax = [0]*n, [0]*n
        for i in range(n):
            for j in range(n):
                if grid[i][j] > rowMax[i]:
                    rowMax[i] = grid[i][j]
                if grid[i][j] > colMax[j]:
                    colMax[j] = grid[i][j]
        total = 0
        for i in range(n):
            for j in range(n):
                total += min(rowMax[i], colMax[j]) - grid[i][j]
        return total
