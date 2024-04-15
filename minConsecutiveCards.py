class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minimum = len(cards)+1
        prefix = {}
        for i in range(len(cards)):
            if cards[i] in prefix:
                minimum = min(i-prefix[cards[i]]+1, minimum)
            prefix[cards[i]] = i
        if minimum == len(cards)+1:
            return -1
        return minimum
