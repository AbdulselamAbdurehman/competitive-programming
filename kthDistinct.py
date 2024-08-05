class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq, unique = {}, []
        for word in arr:
            if word not in freq:
                unique.append(word)
            freq[word] = freq.get(word, 0) + 1
        single = 0
        for key in unique:
            if freq[key] == 1:
                single += 1
            if single == k:
                return key
        return ""
