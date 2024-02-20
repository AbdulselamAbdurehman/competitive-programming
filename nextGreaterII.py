class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        stack, n = [], len(nums)
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                result[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return result
