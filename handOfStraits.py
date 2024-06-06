class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize:
            return False
        freq = Counter(hand)
        new_hand = sorted(freq.keys())
        for card in new_hand:
            while freq[card] > 0:
                for i in range(groupSize):
                    if freq[card + i] == 0:
                        return False
                    freq[card + i] -= 1
        return True
