class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won, lost = {}, {}
        for match in matches:
            winner, loser = match[0], match[1]
            won[winner] = won.get(winner, 0) + 1
            lost[loser] = lost.get(loser, 0) + 1
        zero_loss, one_loss = set(), set()
        for winner in won: 
            if not winner in lost:
                zero_loss.add(winner)
            elif lost[winner] == 1:
                one_loss.add(winner)
        for loser, losses in lost.items():
            if losses == 1:
                one_loss.add(loser)
        return [sorted(zero_loss), sorted(one_loss)]
