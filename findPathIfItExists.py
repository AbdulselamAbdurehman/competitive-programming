class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(curr):
            if curr == destination:
                return True

            visited.add(curr)
            for neighbor in graph[curr]:
                if not neighbor in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)
