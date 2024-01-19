class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1, freq2 = dict(Counter(word1)), dict(Counter(word2))
        for c1 in freq1:
            for c2 in freq2:
                m, n = len(freq1), len(freq2)
                if freq1[c1] == 1 and c2 != c1:
                    m -= 1
                if c2 not in freq1:
                    m += 1
                if freq2[c2] == 1 and c2 != c1:
                    n -= 1
                if c1 not in freq2:
                    n += 1
                if n == m:
                    return True
        return False
