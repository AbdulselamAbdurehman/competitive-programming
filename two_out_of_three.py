class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a, b, c = set(nums1), set(nums2), set(nums3)
        result = []
        for i in a.union(b).union(c):
            if i in a & b or i in b & c or i in a & c:
                result.append(i)
        return result        
