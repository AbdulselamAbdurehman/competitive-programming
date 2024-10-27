class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0, 1, 1]
        for i in range(3, n+1):
            coming = result[-1] + result[-2] + result[-3]
            result.append(coming)
        return result[n]
