class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result, n = 0, len(mat)
        for i in range(n):
            result += mat[i][i] + mat[n-1-i][i]
        if n % 2:
            return result - mat[n//2][n//2]
        return result
