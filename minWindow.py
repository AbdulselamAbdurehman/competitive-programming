class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result, left = [-10, len(s)], 0
        window, freq = Counter(), Counter(t)
        for right in range(len(s)):
            window[s[right]] += 1
            while all([window[char] >= freq[char] for char in freq]):
                if right-left+1 <= result[1] - result[0] + 1:
                    result = [left, right]
                window[s[left]] -= 1
                left += 1
        if result[1] - result[0] <= len(s):
            return s[result[0]:result[1]+1]
        return ""
