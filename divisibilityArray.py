class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        divisibility = []
        rem = 0
        for digit in word:
            rem = rem*10 + int(digit)
            rem = rem % m
            if rem == 0:
               divisibility.append(1)
            else:
                divisibility.append(0) 

        return divisibility
