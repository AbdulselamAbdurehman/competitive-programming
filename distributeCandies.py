class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counter = Counter(candyType)
        return min(len(counter), len(candyType)//2)
