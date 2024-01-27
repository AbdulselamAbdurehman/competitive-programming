class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1), Counter(word2)
        for c in set(word1).union(word2):
            if abs(freq1[c] - freq2[c]) > 3:
                return False
        return True
