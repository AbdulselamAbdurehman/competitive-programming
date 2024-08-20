class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        have = set([(i, j) for j in range(n) for i in range(m)])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def backtrack(x, y, p):
            if board[x][y] != word[p]:
                return False
            
            if p+1 == len(word):
                return True

            have.remove((x, y))
            for dx, dy in directions:
                if (x+dx, y+dy) in have:
                    if backtrack(x+dx, y+dy, p+1):
                        return True

            have.add((x, y))
        print(m, n)
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
