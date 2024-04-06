class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
            else:
                count += j - i
                i += 1
        return count
