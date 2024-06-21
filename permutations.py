class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[] + nums]
        result = []
        for i in range(len(nums)):
            back = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(back)
            result.extend(perms)
            nums.append(back)
        return result
