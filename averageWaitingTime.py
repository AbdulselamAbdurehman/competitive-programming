class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev = waiting = 0
        for customer in customers:
            if customer[0] >= prev:
                prev = customer[0] + customer[1]
            else:
                waiting += prev - customer[0]
                prev += customer[1]
            waiting += customer[1]
        return waiting / len(customers)
