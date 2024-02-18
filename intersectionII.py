class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        result = []
        for num in freq1:
            result.extend([num]*min(freq1.get(num, 0), freq2.get(num, 0)))
        return result
