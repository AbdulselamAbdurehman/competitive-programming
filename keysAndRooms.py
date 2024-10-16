class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Time: O(n) Space: O(n)
        n = len(rooms)
        visited = [False]*n
        dq = deque([0])
        visited[0] = True
        while dq:
            node = dq.popleft()
            for neigh in rooms[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    dq.append(neigh)
        return all(visited)
