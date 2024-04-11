class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = maximum = 0
        zero = -1 #to hold last occurence of zero
        for right in range(len(nums)):
            if nums[right] == 0:
                if zero >= left:
                    left = zero + 1
                zero = right
            maximum = max(maximum, right-left) 
        return maximum
