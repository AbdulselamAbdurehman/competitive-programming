class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = maximum = 0
        for i in range(len(flips)):
            maximum = max(maximum, flips[i])
            if i+1 == maximum:
                count += 1
        return count
