class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = tuple(sorted([start, destination]))
        total = middle = 0
        for i in range(len(distance)):
            if start <= i < destination:
                middle += distance[i]
            total += distance[i]
        return min(middle, total-middle)
