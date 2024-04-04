class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minimum, maximum = min(costs), max(costs)
        freq = Counter(costs)
        remaining, bought = coins, 0
        for ice in range(minimum, maximum+1):
            buy = min(remaining//ice, freq.get(ice, 0))
            bought += buy
            remaining -= buy*ice
        return bought
