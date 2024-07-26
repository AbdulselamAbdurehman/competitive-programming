class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, length = 0, len(flowerbed)
        while i < length:
            left = 0 if i == 0 or flowerbed[i-1] == 0 else 1
            right = 0 if i == length-1 or flowerbed[i+1] == 0 else 1
            if left + right + flowerbed[i] == 0:
                n -= 1
                i += 1
            i += 1
        return n <= 0
                
