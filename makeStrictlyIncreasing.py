class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        n = len(nums)    
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                if removed:
                    return False
                removed = True
                if i == 1 or nums[i] > nums[i - 2]:
                    nums[i - 1] = nums[i]
                elif i == n - 1 or nums[i + 1] > nums[i - 1]:
                    nums[i] = nums[i - 1]
                else:
                    return False
        return True
