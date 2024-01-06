class Solution:
    def average(self, salary: List[int]) -> float:
        minimum, maximum = min(salary), max(salary)
        total = count = 0 
        for val in salary:
            if val != minimum and val != maximum:
                total += val
                count += 1
        return total/count
