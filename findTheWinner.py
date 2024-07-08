class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n+1))
        start = 0
        while len(circle) > 1:
            leaving_index = (start + k - 1) % len(circle)
            circle.pop(leaving_index)
            start = leaving_index
        return circle[0]
