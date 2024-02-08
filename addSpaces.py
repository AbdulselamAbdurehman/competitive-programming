class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        modified = []
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                modified.append(" ")
                j += 1
            modified.append(s[i])
        return "".join(modified)
