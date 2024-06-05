class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])
        for word in words:
            curr_freq = Counter(word)
            for key in freq:
                if curr_freq[key] < freq[key] :
                    freq[key] = curr_freq[key]
        result = []
        for key in freq:
            for _ in range(freq[key]):
                result.append(key)
        return result
