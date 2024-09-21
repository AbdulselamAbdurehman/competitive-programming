class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev_smaller, next_smaller = [-1]*n, [n]*n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        stack = []
        for j in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                next_smaller[j] = stack[-1]
            stack.append(j)

        largest = heights[0]
        for k in range(n):
            largest = max(largest, heights[k]*(next_smaller[k] - prev_smaller[k] - 1))
        return largest
