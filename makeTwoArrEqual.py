class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq_arr, freq_target = Counter(arr), Counter(target)
        return freq_arr == freq_target
