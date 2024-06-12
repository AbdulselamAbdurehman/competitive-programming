class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            operations += 1
        return operations
