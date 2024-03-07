class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        result = []
        for i in range(len(arr)-1, -1, -1):
            result.append(maximum)
            maximum = max(maximum, arr[i])
        result.reverse()
        return result
