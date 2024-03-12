class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = freq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if freq < 2:
                    nums[index] = nums[i]
                    index += 1
                    freq += 1
                else:
                    continue
            else:
                freq = 1
                nums[index] = nums[i]
                index += 1
        return index
