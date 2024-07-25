class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1: 
            mid = len(nums)//2
            left_sub = nums[:mid] 
            right_sub = nums[mid:] 

            self.sortArray(left_sub)
            self.sortArray(right_sub)

            i = j = 0
            for k in range(len(left_sub) + len(right_sub)):
                if j >= len(right_sub) or (i < len(left_sub) and left_sub[i] < right_sub[j]):
                    nums[k] = left_sub[i]
                    i += 1
                else:
                    nums[k] = right_sub[j]
                    j += 1
        return nums
