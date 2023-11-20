class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        incoming = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            if incoming > 0:
                incoming += nums[i]
            else:
                incoming = nums[i]
            maximum = max(incoming, maximum)
        return maximum
