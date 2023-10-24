class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        matrix = []
        for i in range(rows):
            for j in range(cols):
                matrix.append([i, j])
        return sorted(matrix, key=lambda pos: abs(pos[0]-rCenter)+abs(pos[1]-cCenter))
