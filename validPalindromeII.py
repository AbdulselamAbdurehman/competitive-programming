class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                alt1, alt2 = s[left:right], s[left+1:right+1]
                return alt1 == alt1[::-1] or alt2 == alt2[::-1]
            left += 1
            right -= 1
        return True
