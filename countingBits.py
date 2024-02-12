class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            count = 0
            while i > 0:
                i, rem  = divmod(i, 2)
                count += rem
            result.append(count)
        return result
