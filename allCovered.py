class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = {i: False for i in range(left, right+1)}
        for interval in ranges:
            for j in range(interval[0], interval[1]+1):
                if j in covered:
                    covered[j] = True
        return all(covered.values())
