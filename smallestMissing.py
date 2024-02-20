class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix, i = nums[0], 1
        while i < len(nums) and nums[i] == nums[i-1] + 1:
            prefix += nums[i]
            i += 1
        numbers = set(nums)
        while prefix in numbers:
            prefix += 1
        return prefix


        
