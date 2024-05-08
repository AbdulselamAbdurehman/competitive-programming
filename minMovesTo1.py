class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = halved = 0
        while halved < maxDoubles and target > 1:
            if target & 1:
                target -= 1
                moves += 1
            else:
                target //= 2
                moves += 1
                halved += 1
        return moves + target - 1
