class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = 0
        negative = 1
        rearranged = [0]*len(nums)
        for num in nums:
            if num >= 0:
                rearranged[positive] = num
                positive += 2
            else:
                rearranged[negative] = num
                negative += 2
        return rearranged
