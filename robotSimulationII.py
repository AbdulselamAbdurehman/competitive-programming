class Robot:

    def __init__(self, width: int, height: int):
        self.position = 0
        self.perimeter = (width + height - 2)*2
        self.corners = [[0, 0, "South"]]
        for i in range(1, width):
            self.corners.append([i, 0, "East"])
        for i in range(1, height):
            self.corners.append([width-1, i, 'North'])
        for i in range(width-2, -1, -1):
            self.corners.append([i, height-1, 'West'])
        for i in range(height-2, -1, -1):
            self.corners.append([0, i, 'South'])


    def step(self, num: int) -> None:
        self.position += num
    def getPos(self) -> List[int]:
        return self.corners[self.position % self.perimeter][:2]

    def getDir(self) -> str:
        if self.position != 0:
            return self.corners[self.position % self.perimeter][-1]
        if self.position // self.perimeter > 0:
            return self.corner[self.position % self.perimeter][-1]
        return 'East'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
