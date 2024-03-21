class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for i in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        answer = []
        for k in range(m+n-1):
            if k % 2 == 0:
                diagonals[k].reverse()
            answer.extend(diagonals[k])
        return answer
