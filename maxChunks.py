class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_left = -1
        for i in range(len(arr)):
            if i > max_left:
                chunks += 1
            max_left = max(max_left, arr[i]) 

        return chunks
