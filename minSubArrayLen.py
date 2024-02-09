class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        length = 10**5 + 1
        window = 0
        while j < len(nums):
            window += nums[j]
            while window >= target:
                length = min(length, j - i + 1)
                window -= nums[i]
                i += 1
            j += 1
        if length < 10**5 + 1:
            return length
        return 0
