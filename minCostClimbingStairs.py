class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [math.inf]*n
        for i in range(n):
            if i < 2:
                min_cost[i] = cost[i]
            else:
                min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]

        return min(min_cost[-1], min_cost[-2])
