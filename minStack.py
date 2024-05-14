class MinStack:

    def __init__(self):
        self.stack = []
        self.takeover = []

    def push(self, val: int) -> None:
        if not self.takeover or self.stack[self.takeover[-1]] >= val:
            self.takeover.append(len(self.stack))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == self.takeover[-1]:
            self.takeover.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.takeover[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
