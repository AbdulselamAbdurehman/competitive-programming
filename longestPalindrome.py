class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length, odds = 0, False
        for c in freq:
            length += freq[c]
            if freq[c] % 2:
                odds = True
                length -= 1
        return length + odds
