class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        target = Counter(s1)
        window = Counter(s2[:n])
        if window == target:
            return True
            
        for i in range(n, m):
            window[s2[i-n]] -= 1
            window[s2[i]] += 1
            if window == target:
                return True
        return False
