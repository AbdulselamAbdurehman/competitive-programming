class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        maximum = nums[-1]
        replacement = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= maximum:
                maximum = nums[i]
            else:
                k = ceil(nums[i]/maximum)
                replacement += k - 1
                maximum = nums[i]//k
        return replacement
