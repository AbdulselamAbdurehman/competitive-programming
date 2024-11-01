class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) >= 2 and stack[-2] == stack[-1] == s[i]:
                pass
            else:
                stack.append(s[i])
        return "".join(stack)
