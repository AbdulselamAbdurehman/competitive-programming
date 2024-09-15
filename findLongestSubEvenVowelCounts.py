class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        n = longest = 0
        lookup = {0: -1}
        for i in range(len(s)):
            if  s[i] in vowels:
                n ^= 1 << vowels[s[i]]
            if n in lookup:
                longest = max(longest, i - lookup[n])
            else:
                lookup[n] = i
        return longest
