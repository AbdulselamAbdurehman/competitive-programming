class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minimum = math.inf
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
                minimum = min(minimum, nums[right])
            else:
                right = mid - 1
                minimum = min(minimum, nums[mid])
    
        return minimum
