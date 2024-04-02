class Solution:
    def sortSentence(self, s: str) -> str:
        tokens = s.split()
        result = ['']*len(tokens)
        for token in tokens:
            word, digit = self.split(token)
            result[int(digit)-1] = word
        return ' '.join(result)

    def split(self, token):
        for i in range(len(token)):
            if token[i].isdigit():
                return token[:i], token[i:]
