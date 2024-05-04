class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        window = Counter()
        left = count = pairs = 0
        for right in range(len(nums)):
            pairs += window[nums[right]]
            window[nums[right]] += 1
            while pairs >= k:
                window[nums[left]] -= 1
                pairs -= window[nums[left]]
                left += 1
            count += left
        return count
