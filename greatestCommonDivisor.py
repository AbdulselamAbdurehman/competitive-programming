class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        i = 0
        while i < n1 and i < n2:
            if str1[i] != str2[i]:
                return ""
            i += 1
        for j in range(i, n1):
            if str1[j] != str2[(j-i)%n2]:
                return ""
        for k in range(i, n2):
            if str2[k] != str1[(k-i)%n1]:
                return ""
        candidate = str1[:gcd(n1, n2)]
        if str1.count(candidate) * len(candidate) == n1 and str2.count(candidate)*len(candidate) == n2:
            return candidate
        return ""
