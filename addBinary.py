  class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_pair = zip_longest(a[::-1], b[::-1], fillvalue="0")
        carry, result = 0, ""
        for pair in num_pair:
            carry, digit = divmod(int(pair[0]) + int(pair[1]) + carry, 2)
            result += str(digit)
        if carry != 0:
            result += str(carry)
        return result[::-1]
