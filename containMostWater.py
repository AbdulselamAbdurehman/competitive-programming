class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left, right = 0, len(height)-1
        while left < right:
            candidate = min(height[left], height[right])*(right - left)
            maximum = max(candidate, maximum)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum
