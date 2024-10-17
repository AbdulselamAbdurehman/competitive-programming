class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Time: O(1) since O(10_000) == O(1) Space: O(n)
        deadends = set(deadends)

        start = "0000"
        if start in deadends:
            return -1
        dq = deque([[start, 0]]) # [state, steps]
        seen = set([start])
        while dq:
            state, steps = dq.popleft()
            if state == target:
                return steps

            for i in range(4):
                
                upper_state = list(state)
                upper_state[i] = str((int(upper_state[i]) + 1) % 10)
                new_state = "".join(upper_state)
                if not (new_state in seen or new_state in deadends):
                    dq.append([new_state, steps + 1])
                    seen.add(new_state)

                lower_state = list(state)
                lower_state[i] = str((int(lower_state[i]) - 1) % 10)
                new_state = "".join(lower_state)
                if not (new_state in seen or new_state in deadends):
                    dq.append([new_state, steps + 1])
                    seen.add(new_state)


        return -1
