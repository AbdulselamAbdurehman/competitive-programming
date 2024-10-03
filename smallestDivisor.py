class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #Time: O(nlogn), space: O(1)  
        def possible(val):
            result = 0
            for num in nums:
                result += ceil(num/val)
            return result <= threshold
        
        
        low, high = 1, max(nums)
        ans = high
        while low <= high:
            mid = low + (high - low)//2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans
