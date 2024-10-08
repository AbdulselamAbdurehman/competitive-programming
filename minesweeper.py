class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #Time: O(n*m) space: O(n*m) Worst case for recursion stack.
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def countMines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count
        
        def dfs(r, c):
            if board[r][c] != 'E':
                return
            mines = countMines(r, c)
            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        dfs(nr, nc)
        
        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
        else:
            dfs(cr, cc)
        
        return board
