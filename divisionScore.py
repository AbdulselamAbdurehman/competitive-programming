class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones, zeroes = nums.count(1), 0 #as initialization
        result, maximum = [], 0
        for i in range(len(nums)):
            current = ones + zeroes
            if current > maximum:
                result = [i]
                maximum = current
            elif current == maximum:
                result.append(i)
            ones -= nums[i]
            zeroes += 1-nums[i]
        if ones + zeroes > maximum: 
            return [len(nums)]
        elif ones + zeroes == maximum:
            result.append(len(nums))
        return result
