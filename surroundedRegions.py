class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        protected = set()

        def dfs(i, j):
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            protected.add((i, j))
            for dx, dy in directions:
                curr_x, curr_y = i + dx, j + dy
                if 0 <= curr_x < n and 0 <= curr_y < m and board[curr_x][curr_y] == 'O' and not (curr_x, curr_y) in protected :
                    dfs(curr_x, curr_y)


        top = [(0, i) for i in range(m)]
        left = [(i, 0) for i in range(n)]
        right = [(i, m-1) for i in range(n)]
        bottom = [(n-1, i) for i in range(m)]
        borders = top + left + right + bottom
        for r, c in borders:
            if board[r][c] == "O" and not (r, c) in protected:
                dfs(r, c)

    
        for i in range(n):
            for j in range(m):
                if (i, j) not in protected:
                    board[i][j] = 'X'
