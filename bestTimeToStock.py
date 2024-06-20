class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        profitable = prices[0]
        for i in range(len(prices)):
            if prices[i] > profitable:
                total_profit += prices[i] - profitable
            profitable = prices[i]
        return total_profit
