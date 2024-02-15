class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums)
        perimeter, i = sum(nums), len(nums)-1
        while i >= 2:
            perimeter -= arr[i]
            if perimeter > arr[i]:
                return perimeter + arr[i]
            i -= 1

        return -1
