class Solution:
    def minimumLength(self, s: str) -> int:
        dq = deque(s)
        while len(dq) > 1:
            if dq[0] == dq[-1]:
                current = dq[0]
                while dq and dq[0] == current:
                    dq.popleft()
                while dq and dq[-1] == current:
                    dq.pop()
            else:
                return len(dq)
        return len(dq)

