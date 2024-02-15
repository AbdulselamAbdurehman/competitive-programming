class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        minimum = 1
        for num in nums:
            prefix += num
            minimum = min(minimum, prefix)
        if minimum >= 0:
            return 1
        return 1 - minimum
