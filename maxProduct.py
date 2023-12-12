class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = sorted([nums[0], nums[1]], reverse=True)
        for i in range(2, len(nums)):
            if nums[i] > maximum[0]:
                maximum = [nums[i], maximum[0]]
            elif nums[i] > maximum[1]:
                maximum = maximum[:1] + [nums[i]]
        return (maximum[0]-1)*(maximum[1]-1)
