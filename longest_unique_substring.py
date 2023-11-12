class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        taken = {}
        maximum = 0
        for i in range(len(s)):
            if s[i] not in taken:
                taken[s[i]] = i
            else:
                taken = {s[j]: j for j in range(taken[s[i]]+1, i+1)}
            maximum = max(len(taken), maximum)
        return maximum
