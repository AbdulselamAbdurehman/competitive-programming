class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maximum = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if max(str(nums[i]))==max(str(nums[j])):
                    if nums[i] + nums[j] > maximum:
                        maximum = nums[i] + nums[j]
        return maximum
