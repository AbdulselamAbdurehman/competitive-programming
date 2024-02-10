class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        location = {}
        for i, num in enumerate(nums):
            if num in location:
                if abs(location[num]-i) <= k:
                    return True
            location[num] = i
        return False
