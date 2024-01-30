class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": lambda x, y: int(x) + int(y),
                    "-": lambda x, y: int(x)-int(y),
                    "*": lambda x, y: int(x)*int(y),
                    "/": lambda x, y: int(int(x)/int(y)),
                     }
        for token in tokens:
            if token in operators:
                right_arg, left_arg = stack.pop(), stack.pop()
                stack.append(operators[token](left_arg, right_arg))
            else:
                stack.append(token)
        return int(stack.pop())
