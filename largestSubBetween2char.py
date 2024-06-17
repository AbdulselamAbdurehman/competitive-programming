class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        prefix, n = {}, len(s)
        maximum = -1
        for i in range(n):
            if s[i] not in prefix:
                prefix[s[i]] = i
            else:
                maximum = max(i - prefix[s[i]] - 1, maximum)
        return maximum
