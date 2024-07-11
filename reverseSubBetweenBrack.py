class Solution:
    def reverseParentheses(self, s: str) -> str:
        brackets, left = [], []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                brackets.append([left.pop(), i])
        result = list(s)
        for start, end in brackets:
            result[start:end+1] = reversed(result[start:end+1])
        return "".join([c for c in result if (c !='(' and c != ')')])
