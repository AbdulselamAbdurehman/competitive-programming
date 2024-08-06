class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        arr = sorted(freq.values(), reverse=True)
        result = 0
        for i in range(len(arr)):
            result += arr[i]*(i//8 + 1)
        return result
