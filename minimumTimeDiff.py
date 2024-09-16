class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        LAST_MINUTE = 24*60
        stamps = [] #points in minutes
        for point in timePoints:
            hour, minute = map(int, point.split(':'))
            stamps.append(hour*60 + minute)
        stamps.sort()
        minimum = stamps[0] + LAST_MINUTE - stamps[-1]
        for i in range(1, n):
            minimum = min(minimum, stamps[i] - stamps[i-1])
        return minimum 
