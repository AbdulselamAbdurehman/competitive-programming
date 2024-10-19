class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        heights = [[-1]*m for _ in range(n)]
        queue = deque() # Queue of [i, j, height]
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    heights[i][j] = 0

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while queue:
            r, c, height = queue.popleft()
            heights[r][c] = height
            for dx, dy in directions:
                new_x, new_y = r + dx, c + dy
                if 0 <= new_x < n and 0 <= new_y < m and heights[new_x][new_y] == -1:
                    heights[new_x][new_y] = height + 1
                    queue.append((new_x, new_y, height + 1))
        return heights
