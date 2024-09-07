class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0 # the minimu value we may return
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or visited[r][c] or grid[r][c] == 0:
                return 0
            
            directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            visited[r][c] = True
            curr = 1
            for dx, dy in directions:
                curr += dfs(r + dx, c + dy)
            return curr


                


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    result = max(result, dfs(i, j))
        return result
