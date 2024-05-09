class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack, minimum = [], 0
        for half in s:
            if half == '(':
                stack.append(half)
            elif not stack:
                minimum += 1
            else:
                stack.pop()
        return minimum + len(stack)
