class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n, result = len(nums), 0
        prefix = [0]*(n+1)
        for start, end in requests:
            prefix[start] += 1
            prefix[end+1] -= 1
        for i in range(1, n+1):
            prefix[i] += prefix[i-1]
        print(prefix)
        freq, val = sorted(prefix[:-1]), sorted(nums)
        for j in range(n):
            result += freq[j] * val[j]
            result %= (10**9 + 7)
        return result
