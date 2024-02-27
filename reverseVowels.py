class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        sequence = []
        for c in s:
            if c.lower() in vowels:
                sequence.append(c)
        answer = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                answer.append(sequence.pop())
            else:
                answer.append(s[i])
        return ''.join(answer)
        
