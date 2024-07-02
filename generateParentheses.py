class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []

        def backtrack(left, right):
            if len(curr) == 2*n:
                result.append("".join(curr))
                return
            if left < n:
                curr.append('(')
                backtrack(left+1, right)
                curr.pop()
            if right < left:
                curr.append(')')
                backtrack(left, right+1)
                curr.pop()

        backtrack(0, 0)
        return result
