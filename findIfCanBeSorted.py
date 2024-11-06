class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(n-1):
                if nums[j] > nums[j+1] and bin(nums[j]).count('1') == bin(nums[j+1]).count('1'):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                   
                
        return sorted(nums) == nums
