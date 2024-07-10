class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = 0
        for log in logs:
            if log == "../":
                if curr > 0:
                    curr -= 1
            elif log != './':
                curr += 1
        return curr
