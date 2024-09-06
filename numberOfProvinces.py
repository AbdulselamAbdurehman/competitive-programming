class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] and j != i and not visited[j]:
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count
