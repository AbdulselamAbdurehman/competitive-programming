class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins, n = 0, len(piles)
        for i in range(n//3, n, 2):
            coins += piles[i]
        return coins
