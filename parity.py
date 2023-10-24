class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        out_even = []
        out_odd = []
        for i in range(len(nums)):
            if i % 2 == 0 and nums[i] % 2 != 0:
                out_odd.append(i)
            elif i % 2 != 0 and nums[i] % 2 == 0:
                out_even.append(i)
        for j in range(len(out_odd)):
            nums[out_odd[j]], nums[out_even[j]] = nums[out_even[j]], nums[out_odd[j]]
        return nums
