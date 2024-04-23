class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distance = {} # onboard passengers, 
        for numPass, start, end in trips:
            distance[start] = distance.get(start, 0) + numPass
            distance[end] = distance.get(end, 0) - numPass
        east_west = sorted(distance.keys())
        hold = 0
        for place in east_west:
            hold += distance[place]
            if hold > capacity:
                return False
        return True
