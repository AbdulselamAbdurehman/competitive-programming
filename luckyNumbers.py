class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        row_min = [math.inf]*n
        col_max = [-math.inf]*m
        for i in range(n):
            for j in range(m):
                row_min[i] = min(row_min[i], matrix[i][j])
                col_max[j] = max(col_max[j], matrix[i][j])

        luckies = []
        for r in range(n):
            for c in range(m):
                if col_max[c] == row_min[r]:
                    luckies.append(col_max[c])
        
        return luckies
