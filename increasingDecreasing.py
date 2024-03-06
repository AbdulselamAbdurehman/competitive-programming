class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        result, n = [], len(s)
        characters = sorted(freq.keys())
        while n > 0:
            is_going = False
            for i in range(len(characters)):
                char = characters[i]
                if freq[char] > 0:
                    freq[char] -= 1
                    n -= 1
                    result.append(char)
                    is_going = True
            for j in range(len(characters)-1,-1,-1):
                char = characters[j]
                if freq[char] > 0:
                    freq[char] -= 1
                    n -= 1
                    result.append(char)
                    is_going = True
            if not is_going:
                break
        return "".join(result)
