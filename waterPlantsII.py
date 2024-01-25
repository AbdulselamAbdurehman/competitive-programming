class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        fills, n = 0, len(plants)
        canA, canB = capacityA, capacityB 
        for i in range(n//2):
            if canA < plants[i]:
                canA = capacityA
                fills += 1
            if canB < plants[n-1-i]:
                canB = capacityB
                fills += 1
            canA -= plants[i]
            canB -= plants[n-1-i]
        if n % 2 == 1:
            if max(canA, canB) < plants[n//2]:
                fills += 1
        return fills
