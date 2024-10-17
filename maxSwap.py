class Solution:
    def maximumSwap(self, num: int) -> int:
        # Time: O(logn) Space: O(logn)
        val = list(str(num))
        biggest = sorted(val, reverse=True)
        for i in range(len(val)):
            if val[i] != biggest[i]:
                temp = val[i]
                val[i] = biggest[i]
                for j in range(len(val)-1, i, -1):
                    if val[j] == biggest[i]:
                        val[j] = temp
                        return int("".join(val))
        return int("".join(val))
