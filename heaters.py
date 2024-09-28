class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def canWarmWithRadius(radius):
            h = 0 #Pointer for the current heater
            for house in houses:
                while abs(house - heaters[h]) > radius:
                    if heaters[h] > house:
                        return False
                    h += 1
                    if h >= len(heaters):
                        return False
            return True
                


        low, high = 0, max(abs(max(heaters) - min(houses)), abs(min(heaters) - max(houses)))
        answer = high
        while low <= high:
            mid = low + (high - low)//2
            if canWarmWithRadius(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
