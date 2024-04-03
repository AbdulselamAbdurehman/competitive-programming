class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        is_negative = False
        if num < 0:
            num *= -1
            is_negative = True
        val = list(str(num))
        val.sort(reverse=is_negative)
        if is_negative:
            return 0 - int("".join(val))
        zeroes = val.count('0')
        val[zeroes], val[0] = val[0], val[zeroes]
        return int(''.join(val))
