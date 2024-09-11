class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        curr = [] #tracks the queen positions currently used


        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return 
            
            for j in range(n):
                if self.isValidPosition(curr, row, j):
                    curr.append((row, j))
                    backtrack(row+1)
                    curr.pop()




        backtrack(0)
        return count


    def isValidPosition(self, used, i, j):
        for r, c in used:
            if r == i or c == j: #Along the same row or column
                return False
            elif c+r == i+j: #Along a line with slope m = -1
                return False
            elif c-r == j - i: #Along a line with slope m = 1
                return False
        return True
