class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        n = len(word)
        left = longest = 0
        for right in range(n):
            for i in range(max(right - 10, 0), right+1):
                if word[i:right+1] in forbidden:
                    left = max(i + 1, left)
            longest = max(longest, right - left + 1)
        return longest
