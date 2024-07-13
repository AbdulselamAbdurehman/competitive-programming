class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = list(zip(positions, healths, directions, range(1, n+1)))
        robots.sort()
        stack, remaining = [], []
        for robot in robots:
            if robot[2] == 'R':
                stack.append(list(robot))
            else:
                curr = list(robot)
                while stack and stack[-1][1] < curr[1]:
                    stack.pop()
                    curr[1] -= 1
                if stack:
                    if stack[-1][1] == curr[1]:
                        stack.pop()
                    else:
                        stack[-1][1] -= 1
                else:
                    remaining.append(curr)
        remaining.extend(stack)
        result = sorted(remaining, key=lambda rob: rob[3])
        return [rob[1] for rob in result]
