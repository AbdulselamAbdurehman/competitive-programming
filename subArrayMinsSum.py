class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, min_sums = [], []
        answer, PRIME = 0, 10**9 + 7
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
                min_sums.pop()
            if stack:
                sub_arr = arr[i]*(i-stack[-1]) + min_sums[-1]
            else:
                sub_arr = arr[i]*(i+1)
            answer += sub_arr
            answer %= PRIME
            stack.append(i)
            min_sums.append(sub_arr)
        return answer
