class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing, added, i = 1, 0, 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                added += 1
        return added
