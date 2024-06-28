class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        destinations = {i: 0 for i in range(n)}
        for road in roads:
            city1, city2 = road
            destinations[city1] +=  1
            destinations[city2] +=  1
        cities = sorted(destinations.keys(), key=lambda city: destinations[city])

        cities_importance = {cities[i]:i+1 for i in range(n)}
        total_importance = 0
        for road in roads:
            total_importance += cities_importance[road[0]] + cities_importance[road[1]] 
        return total_importance
