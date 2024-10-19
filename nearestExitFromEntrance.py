class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #Time: O(n*m) Space: O(n*m)

        n, m = len(maze), len(maze[0])
        start_r, start_c = entrance
        queue = deque([(start_r, start_c, 0)]) # Queue of [curr_r, curr_c, distance_from_entrance]
        
        seen = [[False]*m for _ in range(n)]
        seen[start_r][start_c] = True
        
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        while queue:
            r, c, distance = queue.popleft()
            if (r == 0 or r == n-1 or c == 0 or c == m-1) and (r != start_r or c != start_c):
                return distance

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < m and maze[new_r][new_c] == '.' and not seen[new_r][new_c]:
                    queue.append((new_r, new_c, distance + 1))
                    seen[new_r][new_c] = True
        
        return -1
