class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        minimum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= minimum:
                minimum = nums[i]
            else:
                max_diff = max(nums[i]-minimum, max_diff)
        return max_diff
