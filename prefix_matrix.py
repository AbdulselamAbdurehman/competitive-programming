class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = self.get_pre_mtx(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return self.prefix[row2][col2]-self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1-1][col1-1]
        elif row1 > 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        elif col1 > 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        return self.prefix[row2][col2]
    def get_pre_mtx(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if i > 0 and j > 0:
                    arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
                elif i > 0:
                    arr[i][j] += arr[i-1][j]
                elif j > 0:
                    arr[i][j] += arr[i][j-1]
        return arr

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
