class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        original = [first]
        for val in encoded:
            new_elem = val ^ original[-1]
            original.append(new_elem)
        return original
