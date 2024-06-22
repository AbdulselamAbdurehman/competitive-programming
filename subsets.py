class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(nums)

    def backtrack(self, arr):
        if not arr:
            return [[]]
        sub_result = self.backtrack(arr[1:])
        result = [[] + sub for sub in sub_result]
        for sub in sub_result:
            sub.append(arr[0])
            result.append(sub)
        return result
