class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = maxReach = 0
        count = 0
        for i in range(len(nums)):
            if reach < i:
                reach = maxReach
                count += 1
            maxReach = max(maxReach, i + nums[i])
        return count
