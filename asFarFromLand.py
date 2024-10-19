class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = [[False]*m for _ in range(m)]

        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j, i, j)) # [(curr_i, curr_j, source_i, source_j)]
                    seen[i][j] = True
        if not queue or len(queue) == n*m:
            return -1
        farthest = 0
        while queue:
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            curr_i, curr_j, source_i, source_j = queue.popleft()
            farthest = max(farthest, abs(source_j - curr_j) + abs(source_i - curr_i))
            for dx, dy in directions:
                new_i, new_j = curr_i + dx, curr_j + dy
                if 0 <= new_i < n and 0 <= new_j < m and not seen[new_i][new_j]:
                    queue.append((new_i, new_j, source_i, source_j))
                    seen[new_i][new_j] = True
        
        return farthest
