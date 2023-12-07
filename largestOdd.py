class Solution:
    def largestOddNumber(self, num: str) -> str:
        largest = ""
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                largest = num[:i+1]
        return largest
