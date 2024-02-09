class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(1, len(nums)):
            maximum = nums[i-1]
            if maximum >= nums[i]:
                operations += maximum + 1 - nums[i]
                nums[i] = maximum + 1
        return operations
