class Solution:
    def pivotInteger(self, n: int) -> int:
        upto_n = n*(n+1)//2
        running = 0
        for i in range(1, n+1):
            running += i
            if running == upto_n - running + i:
                return i
        return -1
