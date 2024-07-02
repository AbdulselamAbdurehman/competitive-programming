class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        n = len(candidates)
        
        def backtrack(amount, start):
            if amount == target:
                result.append(curr + [])
                return
            if amount > target:
                return

            for i in range(start, n):
                curr.append(candidates[i])
                backtrack(amount + candidates[i], i)
                curr.pop()
        
        backtrack(0, 0)
        return result
