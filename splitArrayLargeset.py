class Solution:
    # Time: O(nlogE) where E is the sum of nums
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def possible(val):
            count, curr = 1, 0

            for num in nums:
                if curr + num > val:
                    count += 1
                    curr = 0
                curr += num

            return count <= k


        low, high = max(nums), sum(nums)
        ans = high
        while low <= high:
            mid = low + (high - low)//2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
