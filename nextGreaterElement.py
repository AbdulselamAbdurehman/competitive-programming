class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        lookup = {nums1[i]: i for i in range(len(nums1))}
        queue = []
        for num in nums2:
            while queue and queue[-1] < num:
                result[lookup[queue.pop()]] = num
            if num in lookup:
                queue.append(num)
        return result
