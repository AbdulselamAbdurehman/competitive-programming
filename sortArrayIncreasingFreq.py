class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        arr = list(counter.items())
        print(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i][1] > arr[j][1]:
                    arr[j], arr[i] = arr[i], arr[j]
                elif arr[i][1] == arr[j][1] and arr[i][0] < arr[j][0] :
                    arr[i], arr[j] = arr[j], arr[i]
        result = []
        for key, count in arr:
            result.extend([key]*count)
        return result
