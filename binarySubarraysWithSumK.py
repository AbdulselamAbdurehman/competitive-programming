class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        running = count = 0 # to hold the running total
        for num in nums:
            running += num
            count += prefix.get(running - goal, 0)
            prefix[running] = prefix.get(running, 0) + 1
        return count
