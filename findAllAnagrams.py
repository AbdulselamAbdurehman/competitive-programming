class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n, m = len(s), len(p)
        freq, window = Counter(p), Counter(s[:m])
        if freq == window:
            result.append(0)
        for i in range(m, n):
            add, remove = s[i], s[i-m]
            window[add] += 1
            window[remove] -= 1
            if window == freq:
                result.append(i-m+1)
        return result
