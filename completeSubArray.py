class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        for i in range(len(nums)):
            unique = Counter()
            for j in range(i, len(nums)):
                unique[nums[j]] += 1
                if len(unique) == len(freq):
                    count += 1
        return count
