class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        path = [0]
        def backtrack(curr):
            if path and path[-1] == n - 1:
                result.append(path + [])
                return
            for choice in graph[curr]:
                path.append(choice)
                backtrack(choice)
                path.pop()
        
        backtrack(0)
        return result
