class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        occurrence, n = {}, len(nums)
        for i in range(n):
            if nums[i] in occurrence:
                occurrence[nums[i]].append(i)
            else:
                occurrence[nums[i]] = [i]
        result = [0]*n
        for val in occurrence:
            indices = occurrence[val]
            prefix, suffix, m = 0, sum(indices), len(indices)
            for i in range(m):
                index = indices[i]
                prefix += index
                suffix -= index
                result[index] = suffix + (2*i + 2 - m)*index - prefix
        return result
