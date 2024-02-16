class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = {chr(ord("a")+i):0 for i in range(26)}
        for letter in sentence:
            alphabets[letter] += 1
        for c in alphabets:
            if alphabets[c] == 0:
                return False
        return True
