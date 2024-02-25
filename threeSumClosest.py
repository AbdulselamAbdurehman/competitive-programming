class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest, n = sum(nums[:3]), len(nums)
        for i in range(len(nums)):
            left, right = i+1, n-1
            while left < right:
                triplet =  nums[i] + nums[left] + nums[right]
                if abs(triplet - target) < abs(closest - target):
                    closest = triplet
                if triplet < target:
                    left += 1
                else:
                    right -= 1
        return closest 
                
