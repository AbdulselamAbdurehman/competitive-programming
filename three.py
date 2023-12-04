class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum, i = "", 0
        while i < len(num)-2:
            if len(set(num[i:i+3])) == 1:
                if not maximum:
                    maximum = num[i:i+3]
                elif int(num[i:i+3]) > int(maximum):
                    maximum = num[i:i+3]
            else:
                i += 1
        return maximum
