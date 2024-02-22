class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = binary_or = longest = 0
        for right in range(len(nums)):
            while binary_or & nums[right]:
                binary_or = binary_or & ~nums[left]
                left += 1
            binary_or |= nums[right]
            longest = max(longest, right - left + 1)
        return longest
