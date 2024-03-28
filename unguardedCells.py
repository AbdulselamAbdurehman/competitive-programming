class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        #0, 1, 2 means unguarded, guarded, walled/guard respectively
        for x, y in walls:
            grid[x][y] = 2
        for x, y in guards:
            grid[x][y] = 2
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in guards:
            for dx, dy in directions:
                curr_x, curr_y = x, y
                while 0 <= curr_x+dx < m and 0 <= curr_y+dy < n and grid[curr_x+dx][curr_y+dy] != 2:
                    curr_x += dx
                    curr_y += dy
                    grid[curr_x][curr_y] = 1
        return sum([1 for i in range(m) for j in range(n) if grid[i][j] == 0])
