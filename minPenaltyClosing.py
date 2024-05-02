class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes, no = customers.count('Y'), 0
        minimum, index = yes, 0 #minimum amount and index
        for i in range(1, len(customers)+1): #go checking if closing @index i is optimal
            if customers[i-1] == 'Y':
                yes -= 1
            else:
                no += 1
            if yes + no < minimum:
                minimum, index = yes + no, i
        return index
