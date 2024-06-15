class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        arr, n = sorted(nums), len(nums)
        return min(arr[n-3] - arr[0], arr[n-2] - arr[1], arr[n-1] - arr[2]) #minimize the range
