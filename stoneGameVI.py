class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        realValues = [[aliceValues[i], bobValues[i]] for i in range(n)] #real value is total value given to the stone
        realValues.sort(key=lambda value: value[0] + value[1], reverse=True) #To allow greedy choice
        alicePoints = bobPoints = 0
        for j in range(n):
            if j % 2 == 0:
                alicePoints += realValues[j][0]
            else:
                bobPoints += realValues[j][1]
        if alicePoints > bobPoints:
            return 1
        if alicePoints < bobPoints:
            return -1
        return 0
