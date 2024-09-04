class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocks = set()
        for xb, yb in obstacles:
            blocks.add((xb, yb))

        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        face, curr = 0, [0, 0] #0: North, 1: West, 2: South, 3: East
        maximum = 0

        for cmd in commands:
            if cmd == -2:
                face = (face + 1) % 4
            elif cmd == -1:
                face = (face - 1) % 4
            else:
                dx, dy = directions[face]
                for _ in range(cmd):
                    if (curr[0] + dx, curr[1] + dy) not in blocks:
                        curr[0] += dx
                        curr[1] += dy
                        maximum = max(maximum, curr[0]**2 + curr[1]**2)
                    else:
                        break

        return maximum
