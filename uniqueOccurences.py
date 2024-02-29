class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = dict(Counter(arr))
        return len(freq) == len(set(freq.values()))
