class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] < arr[j] + arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        result = "".join(arr)
        return result if result.count('0') < len(result) else '0'
