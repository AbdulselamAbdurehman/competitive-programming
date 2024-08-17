class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        arr = [(0, 0)] # [(val, index)]
        for i in range(n):
            if s[i] == 'I':
                arr.append((arr[-1][0] + 1, len(arr)))
            else:
                arr.append((arr[-1][0] - 1, len(arr)))
        arr.sort()
        result = [0]*(n+1)
        curr = 0
        for x,y in arr:
            result[y] = curr
            curr += 1
        return result
