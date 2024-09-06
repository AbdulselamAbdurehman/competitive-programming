"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates, value = {}, {}

        for emp in employees:
            subordinates[emp.id] = emp.subordinates
            value[emp.id] = emp.importance

        visited = set()
        def dfs(employee):
            visited.add(employee)
            total = value[employee]

            for sub in subordinates[employee]:
                if not sub in visited:
                    total += dfs(sub)
            return total
        
        return dfs(id)        
