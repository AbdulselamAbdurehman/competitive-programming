class Solution:
    def balancedString(self, s: str) -> int:
        freq= Counter(s)
        minimum = n = len(s)
        if all([val == n//4 for val in freq.values()]):
            return 0
        left = 0
        for right in range(n):
            freq[s[right]] -= 1
            while all([val <= n//4 for val in freq.values()]) and left <= right:
                minimum = min(minimum, right-left+1)
                freq[s[left]] += 1
                left += 1
        return minimum
