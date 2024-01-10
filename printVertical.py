class Solution:
    def printVertically(self, s: str) -> List[str]:
        result = list(zip_longest(*s.split(), fillvalue=" "))
        for i in range(len(result)):
            result[i] = "".join(result[i]).rstrip()
        return result
