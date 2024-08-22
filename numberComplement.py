class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = 0
        for i in range(len(binary)):
            complement *= 2
            if binary[i] == '0':
                complement += 1
        return complement
