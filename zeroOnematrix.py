class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        result = [[-1]*m for _ in range(n)]
        queue = deque() # Queue of (i, j, distance_from_nearest_zero)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    result[i][j] = 0

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while queue:
            r, c, distance = queue.popleft()
            for dx, dy in directions:
                neighbor_x, neighbor_y = r + dx, c + dy
                if 0 <= neighbor_x < n and 0 <= neighbor_y < m and result[neighbor_x][neighbor_y] == -1:
                    result[neighbor_x][neighbor_y] = distance + 1
                    queue.append((neighbor_x, neighbor_y, distance + 1))
        return result
