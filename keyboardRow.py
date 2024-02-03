class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        one_row_words = [] 
        for word in words:
            letters = set(word.lower())
            if letters & row1 == letters or letters & row2 == letters or letters & row3 == letters:
                one_row_words.append(word)
        return one_row_words
