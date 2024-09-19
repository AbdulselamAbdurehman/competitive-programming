class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b
        }
        
        memo = {}
        
        def backtrack(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            
            result = []
            for i in range(left, right + 1):
                if expression[i] in operations:
                    operator = operations[expression[i]]
                    left_part = backtrack(left, i - 1)
                    right_part = backtrack(i + 1, right)
                    
                    for n1 in left_part:
                        for n2 in right_part:
                            result.append(operator(n1, n2))
            
            if not result:
                result.append(int(expression[left:right + 1]))
            
            memo[(left, right)] = result
            return result
        
        return backtrack(0, len(expression) - 1)
