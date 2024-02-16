class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        uniques = sorted(freq.values())
        i = 0
        while i < len(uniques):
            if k >= uniques[i]:
                k -= uniques[i]
            else:
                break
            i += 1
        return len(uniques) - i
