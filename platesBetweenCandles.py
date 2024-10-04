class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Time: O(n + mlogn) Space: O(n + m) result included
        n = len(s)
        candles = [i for i in range(n) if s[i] == '|']
        result = []
        for left, right in queries:
            first = bisect_left(candles, left) #min index of candle in range(left, right]
            last = bisect_right(candles, right) - 1 #max index of candle in range(left, right)
            result.append((candles[last] - candles[first]) - (last - first) if first < last else 0)
        return result
