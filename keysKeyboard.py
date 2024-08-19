class Solution:
    def minSteps(self, n: int) -> int:

        def backtrack(count, clipboard):
            if count == n:
                return 0
            if count > n or clipboard > n:
                return n + 1
            
            opt1 = 1 + backtrack(count + clipboard, clipboard)
            opt2 = 2 + backtrack(count*2, count)

            return min(opt1, opt2)

        if n == 1:
            return 0

        return 1 + backtrack(1, 1)
