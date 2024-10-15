class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Denote Red = 0, Blue = 1
        result = [math.inf]*n
        # Time: O(n) Space: O(n)
        def bfs():
            visited_red = set()
            visited_blue = set()
            dq = deque()
            dq.append([0, 0, 2]) #[node, distance(node, 0, lastColor)] unmatching color for the first case
            while dq:
                node, distance, color = dq.popleft()
                result[node] = min(distance, result[node])
                if color != 0:
                    for neigh in graph[(node, 0)]:
                        if not (node, neigh) in visited_red:
                            dq.append([neigh, distance + 1, 0])
                        visited_red.add((node, neigh))
                if color != 1:
                    for neigh in graph[(node, 1)]:
                        if not (node, neigh) in visited_blue:
                            dq.append([neigh, distance + 1, 1])
                        visited_blue.add((node, neigh))    
        
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[(u, 0)].append(v)
        for u, v in blueEdges:
            graph[(u, 1)].append(v)

        


        bfs()
        for j in range(n):
            if not result[j] < math.inf:
                result[j] = -1
        return result 
