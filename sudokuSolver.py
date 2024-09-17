class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(r, c):
            if r >= 9:
                return True
            if c >= 9:
                return backtrack(r+1, 0)
            if board[r][c] != '.':
                return backtrack(r, c+1)
            for i in range(1, 10):
                candidate = str(i)
                if self.is_valid_move(board, r, c, candidate):
                    board[r][c] = candidate
                    if backtrack(r, c+1):
                        return True
                    board[r][c] = '.'
            


        backtrack(0, 0)



    def is_valid_move(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == val or board[i][col] == val:
                return False
        
        r_start, c_start = (row//3)*3, (col//3)*3
        for i in range(r_start, r_start + 3):
            for j in range(c_start, c_start + 3):
                if board[i][j] == val:
                    return False
        return True
