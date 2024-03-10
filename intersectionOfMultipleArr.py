class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        num_set = list(map(set, nums))
        result = num_set[0]
        for num in list(result):
            for arr in num_set:
                if num not in arr:
                    result.discard(num)
                    break
        return sorted(result)
