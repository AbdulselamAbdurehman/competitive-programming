class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        for i in range(len(nums)):
            if curr < 0:
                return False
            if nums[i] > curr:
                curr = nums[i]
            curr -= 1
        return True
