class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
      #time: O(nlogn) space: O(n)
        n = len(nums)
        sorted_indices = sorted(range(n), key=lambda i: nums[i])

        ans = 0
        min_index = n
        for i in range(n):
            ans = max(ans, sorted_indices[i] - min_index)
            min_index = min(min_index, sorted_indices[i])
        return ans
