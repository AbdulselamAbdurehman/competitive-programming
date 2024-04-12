class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count, n = 0, len(s)
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maximum = count
        for j in range(n-k):
            if s[j] in vowels:
                count -= 1
            if s[j+k] in vowels:
                count += 1
            maximum = max(count, maximum)
        return maximum
