class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        arr = sorted(nums) #just nums sorted
        count, n = 0, len(arr)
        for i in range(1,n):
            if arr[i] <= arr[i-1]:
                count += arr[i-1] - arr[i] + 1
                arr[i] = arr[i-1] + 1
        return count
