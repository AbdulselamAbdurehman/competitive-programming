class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq1, freq2 = Counter(s1.split()), Counter(s2.split())
        ans = []
        for word in freq1:
            if freq1[word] == 1 and not word in freq2:
                ans.append(word)
        for word in freq2:
            if freq2[word] == 1 and not word in freq1:
                ans.append(word)
        return ans
