class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                maximum = sum(nums[i:i+3])
        return maximum
