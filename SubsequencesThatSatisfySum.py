class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #Time: O(nlogn) Space: O(1)
        PRIME = 10**9 + 7
        n = len(nums)
        nums.sort()

        def insert_position(start, val):
            low, high = start, n - 1
            ans = -1
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] <= val:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        count = 0
        for i in range(n):
            curr = insert_position(i, target - nums[i]) - i
            if curr <= -1:
                return count % PRIME
            count = (count + 2**curr)%PRIME
        return count
