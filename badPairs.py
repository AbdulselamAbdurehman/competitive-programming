class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {} # frequency to hold nums[i]-i
        bads = 0
        for i in range(len(nums)):
            val = nums[i] - i
            bads += len(nums) - 1 - i - freq.get(val, 0)
            freq[val] = freq.get(val, 0) + 1
        return bads
