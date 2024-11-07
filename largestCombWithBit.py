class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # we 32 bit numbers , we count every bit, return the maxcount
        bitCount = [0]*32
        for cand in candidates:
            bits = bin(cand)
            j = 0
            for i in range(len(bits)-1, 1, -1):
                bitCount[j] += (bits[i] == '1')
                j += 1
        return max(bitCount)
