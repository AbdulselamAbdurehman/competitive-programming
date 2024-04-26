class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0        
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]
        
        for start in range(cols):
            for end in range(start, cols):
                prefix_sum = defaultdict(int)
                prefix_sum[0] , cur_sum = 1, 0
                for i in range(rows):
                    cur_sum += matrix[i][end] - (matrix[i][start - 1] if start > 0 else 0)
                    count += prefix_sum[cur_sum - target]
                    prefix_sum[cur_sum] += 1
                    
        return count
