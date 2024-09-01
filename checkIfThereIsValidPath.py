class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c):
            if r == n-1 and c == m-1:
                return True

            visited[r][c] = True
            for dx, dy in self.directions[grid[r][c]]:
                new_r, new_c = r + dx, c + dy
                if inbound(new_r, new_c) and not visited[new_r][new_c] and self.can_go(grid, r, c, new_r, new_c):
                    if dfs(new_r, new_c):
                        return True
            return False

        self.directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(1, 0), (0, 1)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        return dfs(0, 0)

    def can_go(self, grid, r1, c1, r2, c2):
        curr, goal = grid[r1][c1], grid[r2][c2]

        if (r2 - r1, c2 - c1) in self.directions[curr]:
            if (r1 - r2, c1 - c2) in self.directions[goal]:
                return True

        return False
