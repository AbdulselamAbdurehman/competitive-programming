class Solution:
    def maximum69Number (self, num: int) -> int:
        val = str(num)
        for i in range(len(val)):
            if val[i] == '6':
                return int(val[:i] + '9' + val[i+1:])
        return num
