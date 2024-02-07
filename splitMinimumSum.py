class Solution:
    def splitNum(self, num: int) -> int:
        num1 = num2 = ""
        num_str = sorted(str(num))
        for i in range(len(num_str)):
            if i % 2 == 0:
                num1 += num_str[i]
            else:
                num2 += num_str[i]
        return int(num1) + int(num2)
