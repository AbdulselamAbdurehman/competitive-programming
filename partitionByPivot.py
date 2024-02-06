class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = equal = 0
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1
        result = [0]*len(nums)
        before, middle, after = 0, less, less + equal
        for val in nums:
            if val > pivot:
                result[after] = val
                after += 1
            elif val == pivot:
                result[middle] = val
                middle += 1
            else:
                result[before] = val
                before += 1
        return result
