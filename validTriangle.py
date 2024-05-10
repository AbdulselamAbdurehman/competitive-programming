class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        arr = sorted(nums)
        answer = 0
        for k in range(2, len(arr)):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]: 
                    answer += j - i
                    j -= 1
                else:
                    i += 1
        return answer
