class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        modified_sentence, i = "", 1
        vowels = set(('a', 'e', 'i', 'o', 'u'))
        for word in sentence.split():
            if word[0].lower() in vowels:
                word = word
            else:
                word = word[1:] + word[0]
            modified_sentence = modified_sentence + " " + word + "ma" + "a"*i
            i += 1
        return modified_sentence.strip()
