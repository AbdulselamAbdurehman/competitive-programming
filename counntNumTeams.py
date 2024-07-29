class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        for i in range(1, n-1):
            # Condition 1 compliant
            left = right = 0
            for j in range(n):
                if j < i and rating[j] < rating[i]:
                    left += 1
                elif j > i and rating[i] < rating[j]:
                    right += 1
            ans += left*right

            # Condition 2 compliant
            left = right = 0
            for j in range(n):
                if j < i and rating[j] > rating[i]:
                    left += 1
                elif j > i and rating[i] > rating[j]:
                    right += 1
            ans += left*right
        return ans
