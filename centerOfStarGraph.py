class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = set()
        for n1, n2 in edges:
            if n1 in nodes:
                return n1
            if n2 in nodes:
                return n2
            nodes.add(n1)
            nodes.add(n2)
