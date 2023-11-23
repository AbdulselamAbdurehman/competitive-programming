class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[j] = nums[k]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
