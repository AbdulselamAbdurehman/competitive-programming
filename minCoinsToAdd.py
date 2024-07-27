class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        minimum, count = 1, 0
        i = 0
        while minimum <= target:
            if i < len(coins) and coins[i] <= minimum:
                minimum += coins[i]
                i += 1
            else:
                minimum += minimum
                count += 1
        return count
