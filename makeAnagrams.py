class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countT, countS = dict(Counter(t)), dict(Counter(s))
        steps = 0
        for c in set(s).union(t):
            steps += abs(countS.get(c, 0)-countT.get(c, 0))
        return steps//2
