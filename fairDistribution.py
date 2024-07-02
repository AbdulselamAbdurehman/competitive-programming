class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        curr = [0]*k
        result = [math.inf]
        n = len(cookies)
        if k == n:
            return max(cookies)
        def backtrack(start):
            if start == n:
                result[0] = min(result[0], max(curr))
                return

            for j in range(k):
                curr[j] += cookies[start]
                backtrack(start + 1)
                curr[j] -= cookies[start]

        backtrack(0)
        return result[0]
