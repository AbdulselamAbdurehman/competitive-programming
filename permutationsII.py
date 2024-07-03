class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        unique = Counter(nums) # value: frequency
        
        def backtrack(curr):
            if len(curr) == n:
                result.append(curr + [])

            for num in unique:
                if unique[num] > 0:
                    unique[num] -= 1
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                    unique[num] += 1

        backtrack([])
        return result
