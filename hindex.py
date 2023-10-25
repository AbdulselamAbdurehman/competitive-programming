class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_arr = sorted(citations, reverse=True)
        num = 0
        for i in range(len(sorted_arr)):
            if sorted_arr[num] > i:
                num += 1
            else:
                return num
        return num
