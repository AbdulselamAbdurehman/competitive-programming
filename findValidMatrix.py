class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [colSum + []]
        n, m = len(rowSum), len(colSum)
        for _ in range(n-1):
            result.append([0]*m)
        rowTotal = sum(colSum)
        for i in range(n-1):
            for j in range(m):
                if rowTotal > rowSum[i]:
                    passover = min(result[i][j], rowTotal - rowSum[i])
                    rowTotal -= passover
                    result[i][j] -= passover
                    result[i+1][j] += passover
                else:
                    break
            rowTotal = 0
            for c in range(m):
                rowTotal += result[i+1][c]
        return result
