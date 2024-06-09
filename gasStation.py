class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        remaining = start = 0
        for i in range(len(gas)):
            remaining += gas[i] - cost[i]
            if remaining < 0:
                remaining, start = 0, i + 1
        return start
