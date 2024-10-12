class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Time: O(nlogn) Space: O(n)
        events = []
        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))
        events.sort()
        max_overlap = curr_max = 0
        for x, i in events:
            curr_max += i
            max_overlap = max(curr_max, max_overlap)
        return max_overlap
