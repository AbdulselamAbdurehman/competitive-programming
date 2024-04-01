class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        result = []
        for num in nums:
            less = self.binary_search(arr, num)
            result.append(less)
        return result

    
    def binary_search(self, arr, num):
        low, mid, high = 0, 0, len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return low
