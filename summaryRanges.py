class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            group = [nums[i]]
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
                group.append(nums[i])
            if len(group) == 1:
                result.append(f"{group[0]}")
            else:
                result.append(f"{group[0]}->{group[-1]}")
            i += 1
        return result
