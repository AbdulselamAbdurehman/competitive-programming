class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq, total = {}, 0
        for num in nums:
            if num in freq:
                repeated = num
            else:
                freq[num] = freq.get(num, 0) + 1
            total += num
        expected = len(nums)*(len(nums)+1)//2
        return [repeated, expected+repeated-total]
