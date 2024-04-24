class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        zeroes, ones = 0, s.count('1')
        for i in range(len(s)-1):
            zeroes += s[i] == '0'
            ones -= s[i] == '1'
            maximum = max(maximum, ones + zeroes)
        return maximum
