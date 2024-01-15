class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1, freq2 = dict(Counter(word1)), dict(Counter(word2))
        if set(freq1.keys()) ^ set(freq2.keys()):
            return False
        return sorted(freq1.values()) == sorted(freq2.values()) 
