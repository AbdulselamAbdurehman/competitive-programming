class Solution:
    def binaryGap(self, n: int) -> int:
        data = bin(n)[2:].strip("0")
        left = maximum = 0
        for i in range(1, len(data)):
            if data[i] == "1":
                maximum = max(maximum, i-left)
                left = i
        return maximum
