class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        pairs = {'a': 'b', 'b':'a'}
        arr = list(s)
        def countSub(sub, p):
            stack = []
            nonlocal points
            for c in arr:
                if stack and stack[-1] in pairs and stack[-1] == sub[0] and pairs[stack[-1]] == c:
                    points += p
                    stack.pop()
                else:
                    stack.append(c)
            return stack     
        if x >= y:
            arr = countSub('ab', x)
            countSub('ba', y)
        else:
            arr = countSub('ba', y)
            countSub('ab', x)
        return points
