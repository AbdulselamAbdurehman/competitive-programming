class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        index1 = sorted(range(n), key=lambda i: nums1[i], reverse=True)
        index2 = sorted(range(n), key=lambda i: nums2[i], reverse=True)

        result = [-1]*n

        i = j = 0 # Pointer for index1 and index2 arr resp.
        for k in range(n):
            num1, num2 = nums1[index1[i]], nums2[index2[j]]
            if num1 > num2:
                result[index2[j]] = num1
                i += 1
            j += 1
        
        for p in range(n):
            if result[p] == -1:
                result[p] = nums1[index1[i]]
                i += 1
        return result
