class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = radiant = 0
        dq = deque(senate)
        while not (dire > 2/3*len(dq) or radiant > 2/3*len(dq)):
            left = dq.popleft()
            if left == 'R':
                if dire > 0:
                    dire -= 1
                else:
                    radiant += 1
                    dq.append(left)
            else:
                if radiant > 0:
                    radiant -= 1
                else:
                    dire += 1
                    dq.append(left)
        if dire > 2/3*len(dq):
            return 'Dire'
        return 'Radiant'
