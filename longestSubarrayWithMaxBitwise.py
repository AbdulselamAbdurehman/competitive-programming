class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        longest = curr = 0
        for i in range(len(nums)):
            if nums[i] == maximum:
                curr += 1
            else:
                curr = 0
            longest = max(curr, longest)
        return longest
