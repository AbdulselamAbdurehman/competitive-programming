class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = prefix = 0
        for num in nums:
            prefix += num
            if prefix == 0:
                count += 1
        return count
