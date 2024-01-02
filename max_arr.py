class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        given = (-1, 1)
        difference = maximum = 0
        prefix = {0:-1}
        for i, num in enumerate(nums):
            difference += given[num]
            if difference in prefix:
                maximum = max(maximum, i - prefix[difference])
            else:
                prefix[difference] = i
        return maximum
