class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colorings = [-1]*n

        def dfs(i, color):
            flag = True
            for neighbor in graph[i]:
                if colorings[neighbor] == color:
                    return False
                elif colorings[neighbor] == -1:
                    colorings[neighbor] = 1 - color
                    flag = flag and dfs(neighbor, colorings[neighbor])
            return flag

        for i in range(n):
            if colorings[i] == -1:
                colorings[i] = 1
                if not dfs(i, colorings[i]):
                    return False
        return True
