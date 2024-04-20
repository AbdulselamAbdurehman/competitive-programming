class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for j in range(len(nums)):
            right -= nums[j]
            if left == right:
                return j
            left += nums[j]
        return -1
