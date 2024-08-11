class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        given = sorted(tokens)
        i, j = 0, len(given)-1
        score = 0
        while i <= j:
            if power >= given[i]:
                power -= given[i]
                i += 1
                score += 1
            elif i < j and score >= 1:
                power += given[j]
                j -= 1
                score -= 1
            else:
                return score
        return score
