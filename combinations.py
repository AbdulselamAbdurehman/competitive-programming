class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        result = []

        def backtrack(i):
            if len(curr) == k:
                result.append(curr + [])
                return

            for j in range(i, n+1):
                curr.append(j)
                backtrack(j+1)
                curr.pop()

        backtrack(1)
        return result
