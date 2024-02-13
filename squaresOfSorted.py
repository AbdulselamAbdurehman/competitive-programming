class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_index = 0
        for i in range(len(nums)):
            nums[i] **= 2
            if nums[i] < nums[min_index]:
                min_index = i

        ans = [nums[min_index]]
        left, right = min_index-1, min_index+1
        while left >= 0 and right < len(nums):
            if nums[left] < nums[right]:
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1
        while right < len(nums):
            ans.append(nums[right])
            right += 1
        while left >= 0:
            ans.append(nums[left])
            left -= 1
        return ans
