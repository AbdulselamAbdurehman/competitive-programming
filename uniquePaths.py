class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                ways = 0
                if i > 0:
                    ways += dp[i-1][j]
                if j > 0:
                    ways += dp[i][j-1]
                if i > 0 or j > 0:
                    dp[i][j] = ways
        return dp[m-1][n-1]
