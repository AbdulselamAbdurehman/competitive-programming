class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maximum = 0
        for num in freq:
            if num+1 in freq:
                maximum = max(maximum, freq[num] + freq[num+1])
        return maximum
