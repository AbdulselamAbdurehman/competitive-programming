class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [0]*len(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        return "".join(shuffled)
