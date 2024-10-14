class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time: O(n^2) space: O(n)
        n = len(s)
        wordSet = set(wordDict)
        cache = {n: True}

        def helper(start):
            if start in cache:
                return cache[start]

            for i in range(start + 1, n + 1):
                if s[start:i] in wordSet:
                    if helper(i):
                        cache[start] = True
                        return True

            cache[start] = False
            return False

        return helper(0)
