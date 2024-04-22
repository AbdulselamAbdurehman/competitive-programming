class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1) #expanded by one to avoid OBOE
        for start, end, seats in bookings: 
            prefix[start-1] += seats # considering the 1-indexed arr given
            prefix[end] -= seats
        answer = [prefix[0]]
        for i in range(1, n):
            prefix[i] += prefix[i-1]
            answer.append(prefix[i])
        return answer
