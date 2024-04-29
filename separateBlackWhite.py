class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = minimum = 0
        for bit in s:
            if bit == "0":
                minimum += ones
            else: 
                ones += 1
        return minimum
