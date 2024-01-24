class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps, can = 0, capacity
        for i in range(len(plants)):
            if plants[i] <= can:
                can -= plants[i]
                steps += 1
            else:
                can = capacity - plants[i]
                steps += 2*i + 1
        return steps
