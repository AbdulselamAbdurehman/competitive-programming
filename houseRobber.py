class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def helper(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            option1 = option2 = option3 = 0
            if i < n:
                option1 = nums[i] + helper(i+2)
            if i+1 < n:
                option2 = nums[i+1] + helper(i+3)
            if i+2 < n:
                option3 = nums[i+2] + helper(i+4) 
            memo[i] = max(option1, option2, option3)
            return memo[i]
            

        return helper(0)
