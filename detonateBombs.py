class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Time: O(n**2), Space: O(n)
        graph = defaultdict(list)
        n = len(bombs)
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2 = bombs[j][0], bombs[j][1]
                    if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                        graph[i].append(j)

        def dfs(node, visited):
            visited.add(node)
            count = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)
            return count
        
        maximum = 0
        for k in range(n):
            visited = set()
            maximum = max(maximum, dfs(k, visited))
        
        return maximum
