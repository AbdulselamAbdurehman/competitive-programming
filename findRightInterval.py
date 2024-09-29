class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n  # By default, no right interval
        indices = sorted(range(n), key=lambda i: intervals[i][0])  # indices of intervals sorted by their start

        for i in range(n):
            ans, curr_end = n, intervals[i][1]
            low, high = 0, n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if curr_end <= intervals[indices[mid]][0]:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if ans < n:
                result[i] = indices[ans]
        
        return result
