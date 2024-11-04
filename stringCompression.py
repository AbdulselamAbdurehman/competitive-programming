class Solution:
    def compressedString(self, word: str) -> str:
        i, n = 0, len(word)
        stack = []
        while i < n:
            j = i
            while j < n and j - i < 9 and word[j] == word[i]:
                j += 1
            stack.append(f'{j - i}'+ word[i])
            i = j
        return "".join(stack)
