class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        n = len(nums)
        for i in range(n//2):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n//2])
        return shuffled
