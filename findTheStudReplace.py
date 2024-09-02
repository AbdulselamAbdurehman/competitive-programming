class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        have = k % sum(chalk) 
        prefix, n = 0, len(chalk)
        for i in range(n):
            if have < chalk[i]:
                return i
            have -= chalk[i]
        return 0
