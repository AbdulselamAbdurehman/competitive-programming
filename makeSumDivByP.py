class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = {0: -1}
        minimum = len(nums)
        rem, running = sum(nums) % p, 0
        for i in range(len(nums)):
            running += nums[i]
            running %= p
            prefix[running] = i
            if (running - rem) % p in prefix:
                minimum = min(minimum, i - prefix[(running - rem) % p])
        return minimum if minimum < len(nums) else -1
