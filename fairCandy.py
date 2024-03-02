class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total, bob_total = sum(aliceSizes), sum(bobSizes)
        delta = alice_total - bob_total
        alice_set = set(aliceSizes)
        for val in bobSizes:
            if val + delta//2 in alice_set:
                return [val + delta//2, val]
