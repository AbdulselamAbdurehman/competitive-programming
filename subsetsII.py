class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        result = [[]]
        for val in freq:
            sub_result = [[val]+res for res in result]
            result.extend(sub_result)
            for i in range(freq[val]-1): #for each additional duplicate
                sub_result = [sub + [val] for sub in sub_result]
                result.extend(sub_result)
        return result
