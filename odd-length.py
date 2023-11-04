class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        even_before, even_after = 1, (n-1)//2
        odd_before, odd_after = 0, n//2
        total = arr[0] * (even_before * (even_after+1))
        for i in range(1, n):
            if i % 2 != 0:
                odd_before += 1
                odd_after -= 1
                total += arr[i] * (even_before * even_after + odd_before * (odd_after + 1))
            else:
                even_before += 1
                even_after -= 1
                total += arr[i] * (even_before * (even_after + 1) + odd_before * odd_after)
        return total

