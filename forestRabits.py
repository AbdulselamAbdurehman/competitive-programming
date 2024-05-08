class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        minimum = 0
        for key in freq:
            if key == 0:
                minimum += freq[key]
            else:
                minimum += ceil(freq[key]/(key + 1)) * (key + 1)
        return minimum
