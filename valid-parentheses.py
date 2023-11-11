class Solution:
    def isValid(self, s: str) -> bool:
        sibling = {"(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{"}
        stack = []
        for item in s:
            if len(stack) > 0 and stack[-1] == sibling[item] and stack[-1] not in ")}]":
                stack.pop()
            else:
                stack.append(item)
        if len(stack) > 0:
            return False
        return True
