class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
        cows = (Counter(guess) & Counter(secret)).total() - bulls
        return f"{bulls}A{cows}B"          
