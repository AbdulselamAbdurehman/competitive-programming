class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(arr), len(queries)
        xors = [0]
        for i in range(n):
            xors.append(xors[-1]^arr[i])
        result = []
        for left, right in queries:
            result.append(xors[right+1]^xors[left])
            
        return result
