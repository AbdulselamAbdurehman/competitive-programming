class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[image[j][i]^1 for i in range(len(image)-1, -1, -1)] for j in range(len(image))]
