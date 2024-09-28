class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    

        def canShipWithCapacity(capacity):
            total , day = 0, 1
            for weight in weights:
                if total + weight > capacity:
                    day += 1
                    total = 0
                total += weight 

            return day <= days
        lower, upper = max(weights), sum(weights) #Lower and Upper bounds of the answer
        answer = upper

        while lower < upper:
            mid = lower + (upper - lower)//2
            if canShipWithCapacity(mid):
                answer = min(answer, mid)
                upper = mid
            else:
                lower = mid + 1
            
        return answer

        

        
