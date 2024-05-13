class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        dq = deque()
        while sorted_deck:
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(sorted_deck.pop())
        return list(dq)
