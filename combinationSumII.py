class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, curr = [], []
        freq = Counter(candidates)
        keys = sorted(freq.keys())
        n = len(keys)

        def backtrack(total, i):
            if total == target:
                result.append(curr + [])
                return
            if total > target:
                return

            for j in range(i, n):
                key, val = keys[j], freq[keys[j]]
                for k in range(1, val+1):
                    curr.append(key)
                    backtrack(total + key*k, j+1)
                
                for _ in range(val):
                    curr.pop()




        for i in range(n):
            key, val = keys[i], freq[keys[i]]
            for j in range(1, val+1):
                curr.append(key)
                backtrack(key*j, i+1)
            
            for _ in range(val):
                curr.pop()

        return result
