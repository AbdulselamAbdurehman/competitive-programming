class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = maximum = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            average = ceil(total/(i+1))
            maximum = max(maximum, average)
        return maximum
