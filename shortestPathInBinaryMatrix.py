class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[n-1][m-1] != 0:
            return -1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dq = deque([(0, 0, 1)]) # List[(x, y, path length)]
        visited = [[False]*m for _ in range(n)]
        while dq:
            r, c, path_length = dq.popleft()
            if r == n-1 and c == m - 1:
                return path_length
            for dx, dy in directions:
                neigh_x, neigh_y = r + dx, c + dy
                if 0 <= neigh_x < n and 0 <= neigh_y < m and grid[neigh_x][neigh_y] == 0 and not visited[neigh_x][neigh_y]:
                    dq.append([neigh_x, neigh_y, path_length + 1])
                    visited[neigh_x][neigh_y] = True
        return - 1
