class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        maximum = curr = 0 # find k-length substring with highest #Black
        for i in range(len(blocks)):
            if blocks[i] == 'B':
                curr += 1
            if i >= k and blocks[i-k] == 'B':
                curr -= 1
            maximum = max(maximum, curr)
        return k-maximum
