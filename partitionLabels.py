class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left, n = 0, len(s)
        result = []
        while left < n:
            right, lookup = left, set([s[left]])
            for i in range(left, n):
                if s[i] in lookup:
                    lookup = lookup.union(set(s[right: i+1]))
                    right = i
            result.append(right - left + 1)
            left = right + 1
        return result
