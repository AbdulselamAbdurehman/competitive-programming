class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or visited[r][c] or grid[r][c] == '0':
                return
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            visited[r][c] = True
            for dx, dy in directions:
                dfs(r + dx, c + dy)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count
