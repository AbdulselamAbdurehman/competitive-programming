class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        positions = {letter: i for i, letter in enumerate(order)}
        representation = []
        for word in words:
            representation.append([positions[let] for let in word])
        if sorted(representation) == representation:
            return True
        return False
