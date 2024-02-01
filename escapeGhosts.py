class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            if abs(ghost[0]-target[0]) + abs(ghost[1]-target[1]) <= abs(target[0]) + abs(target[1]):
                return False
        return True
