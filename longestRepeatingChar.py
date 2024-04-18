class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum = left = 0
        freq = {'A': 0}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while right - left + 1 - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            maximum = max(maximum, right-left+1)
        return maximum
