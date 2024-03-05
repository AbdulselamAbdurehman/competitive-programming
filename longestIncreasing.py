class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 1
        left = 0
        for right in range(1, len(nums)):
            if nums[right-1] < nums[right]:
                max_length = max(max_length, right-left+1)
            else:
                left = right
        return max_length
