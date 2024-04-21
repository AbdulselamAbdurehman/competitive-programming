class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        for shift in shifts:
            up, down = shift[0], shift[1]+1
            if shift[2] == 0:
                prefix[up] -= 1
                prefix[down] += 1
            else:
                prefix[up] += 1
                prefix[down] -= 1
        result = [self.shift_char(s[0], prefix[0])]
        for i in range(1, len(s)):
            prefix[i] += prefix[i-1]
            result.append(self.shift_char(s[i], prefix[i]))
        return ''.join(result)


    def shift_char(self, char, i):
        return chr((ord(char) - ord('a') + i)%26 + ord('a')) #cyclic shifting
