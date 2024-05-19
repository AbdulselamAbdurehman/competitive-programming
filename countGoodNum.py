class Solution:
    def countGoodNumbers(self, n: int) -> int:
        PRIME = 10**9 + 7
        result = self.modExp(5, (n-1)//2 + 1, PRIME) * self.modExp(4, n//2, PRIME)
        return result % PRIME
    def modExp(self, a, b, n):
        result = 1
        base = a % n
        while b > 0:
            if b % 2 == 1:
                result = (result * base) % n
            base = (base * base) % n
            b = b // 2
        return result
