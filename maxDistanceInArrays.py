class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum, maximum = math.inf, -math.inf
        answer = 0
        for arr in arrays:
            curr_min, curr_max = arr[0], arr[-1]
            if maximum - curr_min >= answer:
                answer = maximum - curr_min
            if curr_max - minimum >= answer:
                answer = curr_max - minimum
            
            minimum = min(minimum, curr_min)
            maximum = max(maximum, curr_max)
        return answer
