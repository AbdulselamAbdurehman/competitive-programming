class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n1, n2, n3, = len(s1), len(s2), len(s3)
        n = min(n1, n2, n3)
        i = 0
        while i < n and s1[i] == s2[i] == s3[i]:
            i += 1
        if i == 0:
            return -1
        return n1 + n2 + n3 - 3*i
