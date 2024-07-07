class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_num = numBottles
        while numBottles >= numExchange:
            full, empty = divmod(numBottles, numExchange)
            max_num += full
            numBottles = full + empty
        return max_num
