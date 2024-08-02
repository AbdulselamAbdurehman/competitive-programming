class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        window = 0
        for i in range(ones):
            if nums[i]:
                window += 1
        answer = window
        for j in range(n):
            window -= nums[j] - nums[(j+ones)%n]
            answer = max(answer, window)
        return ones - answer
