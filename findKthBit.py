class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        nth, i = '0', 1
        if n == 1:
            return nth
        while i < n:
            nth = nth + '1' + self.reverseBit(self.invertBit(nth))
            i += 1
        return nth[k-1]
        
    def reverseBit(self, bits):
        return bits[::-1]
    
    def invertBit(self, bits):
        return "".join([('0' if bit == '1' else '1') for bit in bits])
