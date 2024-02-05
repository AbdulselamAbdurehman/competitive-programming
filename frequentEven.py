class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
        minimum, frequency = None, 0
        for num in freq:
            if minimum == None:
                frequency, minimum = freq[num], num
            elif freq[num] > frequency or freq[num] == frequency and num < minimum:
                frequency, minimum = freq[num], num
        if minimum == None:
            return -1
        return minimum
