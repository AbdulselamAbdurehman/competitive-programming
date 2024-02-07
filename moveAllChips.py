class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_position = even_position = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even_position += 1
            else:
                odd_position += 1
        return min(even_position, odd_position)
