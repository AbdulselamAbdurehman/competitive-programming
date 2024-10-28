class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totals = {0: 1}
        
        for num in nums:
            new_totals = {}
            for total, count in totals.items():
                new_totals[total + num] = new_totals.get(total + num, 0) + count
                new_totals[total - num] = new_totals.get(total - num, 0) + count
            totals = new_totals
        
        return totals.get(target, 0)
