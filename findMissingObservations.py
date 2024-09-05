class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        missing_sum = total - sum(rolls)
        avg, rem = divmod(missing_sum, n)
        if avg < 1 or avg > 6 or (avg == 6 and rem > 0):
            return []
        result = []
        for i in range(n):
            if i < rem:
                result.append(avg + 1)
            else:
                result.append(avg)
        return result
