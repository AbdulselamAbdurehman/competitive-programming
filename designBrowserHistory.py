class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.index = 0
        

    def visit(self, url: str) -> None:
        self.visited = self.visited[:self.index+1]
        self.visited.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps, 0)
        return self.visited[self.index]
        
    def forward(self, steps: int) -> str:
        self.index = min(self.index + steps, len(self.visited)-1)
        return self.visited[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
