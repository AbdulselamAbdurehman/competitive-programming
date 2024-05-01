class Solution:
    def numberOfWays(self, s: str) -> int:
        oneRight, zeroRight = s.count('1'), s.count('0')
        oneLeft = zeroLeft = count = 0
        for bit in s:
            if bit == '0':
                count += oneLeft*oneRight
                zeroLeft += 1
                zeroRight -= 1
            else: 
                count += zeroLeft*zeroRight
                oneLeft += 1
                oneRight -= 1
        return count
