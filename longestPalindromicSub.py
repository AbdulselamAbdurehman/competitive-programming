class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0
        for i in range(n):
            i_center = self.expand(s, i, i)
            if i_center[1] - i_center[0] > ans_right - ans_left:
                ans_left, ans_right = i_center
            if i+1 < n and s[i] == s[i+1]:
                even = self.expand(s, i, i+1)
                if even[1] - even[0] > ans_right - ans_left:
                    ans_left, ans_right = even
            if i-1 >= 0 and s[i] == s[i-1]:
                even = self.expand(s, i-1, i)
                if even[1] - even[0] > ans_right - ans_left:
                    ans_left, ans_right = even
        
        return s[ans_left:ans_right+1]




    def expand(self, s, left, right):
        n = len(s)
        while left-1 >= 0 and right+1 < n and s[left-1] == s[right+1]:
            left -= 1
            right += 1
        return (left, right)
