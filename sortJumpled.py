class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def getMappedValue(num):
            val = [mapping[int(digit)] for digit in str(num)]
            ans = 0
            for d in val:
                ans *= 10
                ans += d
            return ans
        ans = [[getMappedValue(nums[i]), i] for i in range(len(nums))]
        ans.sort()
        result = [nums[i] for val, i in ans]
        return result
