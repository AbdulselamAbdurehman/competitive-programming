class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n, m = len(difficulty), len(worker)
        works = sorted(range(n), key=lambda i: difficulty[i]) #sorted difficulty index
        worker.sort()
        i = j = 0
        max_profit = profitable = 0
        while i < n and j < m:
            if difficulty[works[i]] > worker[j]:
                max_profit += profitable
                j += 1
            else:
                profitable = max(profitable, profit[works[i]])
                i += 1
        max_profit += (m-j)*profitable
        return max_profit
