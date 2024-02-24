class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sequence = sorted(nums)
        return sequence[-1]*sequence[-2] - sequence[0]*sequence[1]
