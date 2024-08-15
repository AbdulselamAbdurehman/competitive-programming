class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        have = list(range(1, 10))
        length = 9
        result, curr = [], []

        def backtrack(i, total):
            if total == n and len(curr) == k:
                result.append(curr + [])
                return
            elif total > n or len(curr) > k:
                return

            for j in range(i, length):
                curr.append(have[j])
                backtrack(j+1, total + have[j])
                curr.pop()

        backtrack(0, 0)
        return result
