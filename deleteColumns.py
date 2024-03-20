class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletions = 0
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i-1][j]:
                    deletions += 1
                    break
        return deletions
