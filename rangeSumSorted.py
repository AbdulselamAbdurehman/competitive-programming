class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        PRIME = 10**9 + 7
        subarray_sums = []
        n = len(nums)
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                subarray_sums.append(curr)
        subarray_sums.sort()
        result = 0
        for k in range(left-1, right):
            result += subarray_sums[k]
            result %= PRIME
        return result
