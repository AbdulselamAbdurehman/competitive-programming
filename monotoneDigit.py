class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        stack = []
        digits = str(n)
        for digit in digits:
            if not stack or stack[-1] <= digit:
                stack.append(digit)
            else:
                current = digit
                while stack and stack[-1] > current:
                    current = f"{int(stack.pop())-1}"
                stack.append(current)
                for j in range(len(stack), len(digits)):
                    stack.append('9')
                return int(''.join(stack))
        return int(''.join(stack))
