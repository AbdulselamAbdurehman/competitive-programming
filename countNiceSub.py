class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        odd_count = nice_count = 0
        for num in nums:
            parity = num % 2
            odd_count += parity
            nice_count += prefix.get(odd_count - k, 0)
            prefix[odd_count] = prefix.get(odd_count, 0) + 1
        return nice_count
