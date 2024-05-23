class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        cache = {}

        def score(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]

            taking_left = nums[left] - score(left + 1, right)
            taking_right = nums[right] - score(left, right - 1)
            cache[(left, right)] = max(taking_left, taking_right) 
            return cache[(left, right)]


        return score(0, len(nums)-1) >= 0
