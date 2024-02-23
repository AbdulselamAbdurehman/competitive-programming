class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        p2s, s2p = {}, {}
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern[i] in p2s:
                if p2s[pattern[i]] != words[i]:
                    return False
            if words[i] in s2p:
                if s2p[words[i]] != pattern[i]:
                    return False
            p2s[pattern[i]] = words[i]
            s2p[words[i]] = pattern[i]
        return True
