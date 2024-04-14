class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = maximum = curr = 0
        window = {}
        for right in range(len(nums)):
            val = nums[right]
            if val in window:
                new_left = window[val] + 1
                for i in range(left, window[val]+1):
                    curr -= nums[i]
                    del window[nums[i]]
                left = new_left
            window[val] = right
            curr += val
            maximum = max(maximum, curr)
        return maximum
