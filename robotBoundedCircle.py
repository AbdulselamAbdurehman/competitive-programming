class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pointer = 0
        for instruction in instructions:
            if instruction == 'G':
                position[0] += directions[pointer][0]
                position[1] += directions[pointer][1]
            elif instruction == 'R':
                pointer = (pointer - 1) % 4
            else:
                pointer = (pointer + 1) % 4
        if pointer != 0 or position == [0, 0]:
            return True
        return False
