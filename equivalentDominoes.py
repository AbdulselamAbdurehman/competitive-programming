class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        equivalent = {}
        for domino in dominoes:
            pair = (min(domino), max(domino))
            equivalent[pair] = equivalent.get(pair, 0) + 1
        answer = 0
        for dom in equivalent:
            answer += equivalent[dom]*(equivalent[dom]-1)//2
        return answer
