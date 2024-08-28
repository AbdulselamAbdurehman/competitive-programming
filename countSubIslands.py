class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid2[r][c] == 0 or visited[r][c]:
                return True
            visited[r][c] = True
            result = True
            if grid1[r][c] == 0:
                result = False
            result = dfs(r-1, c) and result
            result = dfs(r+1, c) and result
            result = dfs(r, c-1) and result
            result = dfs(r, c+1) and result
            return result

        visited = [[False]*cols for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and not visited[r][c] and dfs(r, c):
                    count += 1
        return count
