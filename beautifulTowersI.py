class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        increasing, stack = [-1]*n, []
        
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            if stack:
                increasing[i] = heights[i] * (i - stack[-1]) + increasing[stack[-1]]
            else:
                increasing[i] = heights[i] * (i + 1)
            stack.append(i)
        
        decreasing, stack = [-1]*n, []
        for j in range(n-1, -1, -1):
            while stack and heights[stack[-1]] > heights[j]:
                stack.pop()
            if stack:
                decreasing[j] = heights[j] * (stack[-1] - j) + decreasing[stack[-1]]
            else:
                decreasing[j] = heights[j] * (n - j)
            stack.append(j)

        max_sum = 0
        for i in range(n):
            max_sum = max(max_sum, increasing[i] + decreasing[i] - heights[i])

        return max_sum

