class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        material = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for letter in text:
            if letter in material:
                material[letter] += 1
        cost = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        maximum = len(text)
        for item in material:
            maximum = min(maximum, material[item]//cost[item])
        return maximum
