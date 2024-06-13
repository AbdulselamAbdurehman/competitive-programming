class Solution:
    def nthUglyNumber(self, n: int) -> int:
        k, curr = 1, 1
        seen = set()
        factors2, factors3, factors5 = set(), set(), set()
        while k < n:
            seen.add(curr)
            factors2.discard(curr)
            factors3.discard(curr)
            factors5.discard(curr)
            by_2, by_3, by_5 = curr*2, curr*3, curr*5
            if by_2 not in seen:
                factors2.add(by_2)
            if by_3 not in seen:
                factors3.add(by_3)
            if by_5 not in seen:
                factors5.add(by_5)
            k += 1
            curr = min(min(factors2), min(factors3), min(factors5))
        return curr
