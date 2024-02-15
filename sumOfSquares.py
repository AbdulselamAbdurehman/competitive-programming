class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 2:
            return True
        seen = set()
        for i in range(math.ceil(c**0.5)+1):
            if c-i**2 in seen:
                return True
            if 2*i**2 == c:
                return True
            seen.add(i**2)
        return False
