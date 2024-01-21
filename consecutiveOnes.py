class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = length = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                length = 0
            if length > maximum:
                maximum = length
        return maximum
