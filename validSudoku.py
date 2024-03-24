    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns, rows = [], [] # To validate on rows and columns 
        for i in range(9):
            columns.append(set())
            rows.append(set())
        boxes = [[set() for i in range(3)] for j in range(3)] # To validate on 3x3 boxes
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in columns[j]:
                    return False
                if board[i][j] in boxes[i//3][j//3]:
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[i//3][j//3].add(board[i][j])
        return True
