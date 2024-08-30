class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        result = []
        taken = [] # Positions already occupied by queens
        def is_valid_position(r, c):
            for x, y in taken:
                if y == c:
                    return False
                if r - c == x - y:
                    return False
                if r + c == x + y:
                    return False

            return True



        def backtrack(r, q):
            if q == n:
                temp = ["".join(row) for row in board]
                result.append(temp)
                return

            for c in range(n):
                if is_valid_position(r, c):
                    board[r][c] = 'Q'
                    taken.append((r, c))
                    backtrack(r+1, q+1)
                    taken.pop()
                    board[r][c] = '.'             
            
            

        backtrack(0, 0)
        return result
