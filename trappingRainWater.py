class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        for high in reversed(height):
            stack.append(max(stack[-1], high))
        
        amount = max_left = 0
        for high in height:
            stack.pop()
            amount += max(min(max_left, stack[-1]) - high, 0)
            max_left = max(max_left, high)
        
        return amount
