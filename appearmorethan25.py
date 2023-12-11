class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        count, prev = 1, arr[0]
        for i in range(1, len(arr)):
            if arr[i] != prev:
                count = 0
            count += 1
            prev = arr[i]
            if count > len(arr)*0.25:
                return prev

