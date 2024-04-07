class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, count = 0, len(nums)-1, 0
        while i < j:
            curr = nums[i] + nums[j] 
            if curr == k:
                count += 1
                i += 1
                j -= 1
            elif curr < k:
                i += 1
            else:
                j -= 1 
        return count
