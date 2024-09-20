class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.subArrayMaxSums(nums) - self.subArrayMinSums(nums)

    def subArrayMinSums(self, nums):
        n = len(nums)
        min_sum = 0
        stack = []
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] > nums[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                count = (mid - left) * (right - mid)
                min_sum += nums[mid] * count
            stack.append(i)
        return min_sum

    def subArrayMaxSums(self, nums):
        n = len(nums)
        max_sum = 0
        stack = []
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] < nums[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                count = (mid - left) * (right - mid)
                max_sum += nums[mid] * count
            stack.append(i)
        return max_sum
