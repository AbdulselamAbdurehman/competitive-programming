class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, denominator = 0, 1

        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                if expression[i] == '-':
                    sign = -1
                i += 1

            num_start = i
            while expression[i].isdigit():
                i += 1
            num = int(expression[num_start:i])

            i += 1

            denom_start = i
            while i < len(expression) and expression[i].isdigit():
                i += 1
            denom = int(expression[denom_start:i])

            numerator = numerator * denom + sign * num * denominator
            denominator *= denom

            common_divisor = gcd(abs(numerator), denominator)
            numerator //= common_divisor
            denominator //= common_divisor

        return f"{numerator}/{denominator}"
