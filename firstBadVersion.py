# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower, higher = 1, n
        while lower < higher:
            mid = lower + (higher - lower)//2
            if isBadVersion(mid):
                higher = mid
            else:
                lower = mid + 1
        return lower
