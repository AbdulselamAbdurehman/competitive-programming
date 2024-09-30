class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Time: O(logn)
        #Space: O(1)
        result = min(citations[0], 1)
        n = len(citations)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low)//2
            if n - mid == citations[mid]:
                return citations[mid]
            elif n - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
            result = max(result, min(n - mid, citations[mid]))
        return result
