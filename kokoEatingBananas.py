class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatWithSpeed(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile/speed)
            
            return hours <= h
        
        low, high = 1, max(piles)
        answer = high
        while low <= high:
            mid = low + (high - low)//2
            if canEatWithSpeed(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer
