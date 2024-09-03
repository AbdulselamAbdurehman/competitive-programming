class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = ""
        for c in s:
            total += str(ord(c) - ord('a') + 1)
        for i in range(k):
            total = f"{sum([int(d) for d in total])}"
        return int(total)
