class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        common = set(s).union(set(t))
        for ch in common:
            if s.count(ch) != t.count(ch):
                return False
        return True
