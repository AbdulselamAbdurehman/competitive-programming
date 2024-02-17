class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack:
                if stack[-1] != c and stack[-1].upper() == c.upper():
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)
