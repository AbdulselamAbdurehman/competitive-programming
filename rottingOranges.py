class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        fresh = sum([1 for i in range(n) for j in range(m) if grid[i][j] == 1])
        rotten = deque([[i, j] for i in range(n) for j in range(m) if grid[i][j] == 2])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        minutes = 0

        while rotten:
            if fresh == 0:
                return minutes
            minutes += 1
            for i in range(len(rotten)):
                curr_x, curr_y = rotten.popleft()
                for dx, dy in directions:
                    neigh_x, neigh_y = curr_x + dx, curr_y + dy
                    if 0 <= neigh_x < n and 0 <= neigh_y < m and grid[neigh_x][neigh_y] == 1:
                        grid[neigh_x][neigh_y] = 2
                        rotten.append([neigh_x, neigh_y])
                        fresh -= 1
        if fresh:
            return -1
        return minutes
