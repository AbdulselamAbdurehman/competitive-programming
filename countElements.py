class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maximum, total = freq[nums[0]], 0
        for val in freq:
            if freq[val] == maximum:
                total += maximum
            elif freq[val] > maximum:
                total = maximum = freq[val]
        return total
