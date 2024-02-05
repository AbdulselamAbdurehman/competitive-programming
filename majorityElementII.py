class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majorities = set()
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > len(nums)/3:
                majorities.add(num)   
        return list(majorities)
