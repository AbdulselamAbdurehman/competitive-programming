class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lookup = set(dictionary)
        result, words = [], sentence.split()
        for word in words:
            i, n = 0, len(word)
            while i < n and word[:i+1] not in lookup:
                i += 1
            result.append(word[:i+1])
        return " ".join(result)
