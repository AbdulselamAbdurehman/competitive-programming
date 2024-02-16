class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            uppers, lowers = set(), set()
            for j in range(i, len(s)):
                if s[j].islower():
                    lowers.add(s[j].upper())
                else:
                    uppers.add(s[j])
                if lowers == uppers and j-i+1 > len(longest):
                    longest = s[i:j+1]
        return longest
