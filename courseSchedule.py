class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        colors = [0]*numCourses
        #0: not visited, 1: currently being visited, 2: already visited
        def dfs(index):


            for adj in graph[index]:
                if colors[adj] == 2:
                    continue
                if colors[adj] == 1:
                    return False
                colors[adj] = 1
                if not dfs(adj):
                    return False
                colors[adj] = 2
            
            return True



        for i in range(numCourses):
            if colors[i] == 0:
                colors[i] = 1
                if not dfs(i):
                    return False
                colors[i] += 1
        return True
