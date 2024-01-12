class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        return sum([1 for i in range(len(s)//2) if s[i] in vowels]) == sum([1 for i in range(len(s)//2, len(s)) if s[i] in vowels])
