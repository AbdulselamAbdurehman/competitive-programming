class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        missing = 1 #least number we're missing == max consecutive integers we can make
        for coin in coins:
            if coin > missing:
                return missing
            missing += coin
        return missing
