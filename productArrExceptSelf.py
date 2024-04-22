class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [nums[0]], [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i])
        for j in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1]*nums[j]) 
        suffix.reverse()
        result = []
        for k in range(len(nums)):
            left = right = 1
            if k > 0:
                left = prefix[k-1]
            if k < len(nums)-1:
                right = suffix[k+1]
            result.append(right*left)
        return result
