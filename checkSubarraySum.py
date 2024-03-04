class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulo = {0: -1}
        prefix, n = 0, len(nums)
        for i in range(n):
            prefix += nums[i]
            prefix %= k
            if prefix in modulo:
                if i - modulo[prefix] >= 2:
                    return True
            else:
                modulo[prefix] = i
        return False
