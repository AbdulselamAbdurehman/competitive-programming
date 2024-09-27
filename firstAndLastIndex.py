class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first = self.firstIndex(nums, target)
        last = self.lastIndex(nums, target)

        return [first, last]



    def firstIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        
        if left < len(nums) and nums[left] == target:
            return left
        return -1

    def lastIndex(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0 and nums[right] == target:
            return right
        return -1
