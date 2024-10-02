class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Time: O(log(n*m)) Space: O(1)
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols - 1
        while low <= high:
            mid = low + (high - low)//2
            curr = matrix[mid//cols][mid%cols]
            if curr == target:
                return True
            elif curr > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
