class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        result = [nums[dq[0]]]
        for j in range(k, n):
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()
            dq.append(j)
            if dq[-1] - dq[0] == k:
                dq.popleft()
            result.append(nums[dq[0]])
        return result
