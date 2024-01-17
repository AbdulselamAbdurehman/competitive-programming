class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += [i]
            if len(diff) > 2:
                return False
        if len(diff) == 0:
            return True
        if len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]:
            return True
        return False
