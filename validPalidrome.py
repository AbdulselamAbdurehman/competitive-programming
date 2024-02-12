class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure = ""
        for c in s:
            if c.isalnum():
                if c.isalpha():
                    c = c.lower()
                pure += c
        return pure == pure[::-1]
