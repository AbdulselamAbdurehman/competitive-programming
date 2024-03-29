class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        decreasing_heights = sorted(range(len(heights)), key=lambda item: heights[item], reverse=True)
        result = []
        for height in decreasing_heights:
            result.append(names[height])
        return result
