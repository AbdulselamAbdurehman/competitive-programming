class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = list(map(int, str(k)))[::-1]
        num = num[::-1]
        carry = 0
        result = []
        for i in range(max(len(k), len(num))):
            a = b = 0
            if i < len(num):
                a = num[i]
            if i < len(k):
                b = k[i]
            result.append((a+b+carry)%10)
            carry = (a+b+carry)//10
        if carry > 0:
            result.append(carry)
        return result[::-1]
