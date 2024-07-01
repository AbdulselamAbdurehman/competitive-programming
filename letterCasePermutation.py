class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        curr, n = list(s), len(s)

        def backtrack(i):
            if i == n:
                result.append("".join(curr))
                return
            if curr[i].isdigit():
                backtrack(i+1)
                return
            original = curr[i]
            options = [original.lower(), original.upper()]
            for option in options:
                curr[i] = option
                backtrack(i+1)

        backtrack(0)
        return result
