class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_diff = sorted(costs, key=lambda cost: cost[1] - cost[0])
        total_cost, n = 0, len(costs)
        for i in range(n):
            if i < n//2:
                total_cost += cost_diff[i][1]       
            else:
                total_cost += cost_diff[i][0]
        return total_cost
