class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = (time // (n-1)) % 2 # 1: forward, 0: backward
        if direction:
            return n - time % (n-1)
        return time % (n-1) + 1
