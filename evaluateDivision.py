class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            nume, deno, val = equations[i][0], equations[i][1], values[i]
            graph[nume].append([deno, val])
            graph[deno].append([nume, 1 / val])

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1.0
            q = deque([[src, 1.0]]) 
            visited = set([src])
            while q:
                node, curr_val = q.popleft()
                if node == target:
                    return curr_val 
                    
                for neighbor, value in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append([neighbor, curr_val * value])
            return -1.0
        result = []
        for src, target in queries:
            result.append(bfs(src, target))

        return result
