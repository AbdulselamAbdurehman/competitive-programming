class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        i, n = 0, len(formula)
        while i < n:
            if formula[i] == '(':
                stack.append(['(', 0])
            elif formula[i] == ')':
                val, j = self.getNumber(formula, i+1)
                temp = []
                while stack[-1][0] != '(':
                    top = stack.pop()
                    top[1] *= val
                    temp.append(top)
                stack.pop()
                stack.extend(temp)
                i = j-1
            else:
                j = i+1
                while j < n and formula[j].islower():
                    j += 1
                element = formula[i:j]
                freq, end = self.getNumber(formula, j)
                stack.append([element, freq])
                i = end - 1
            i += 1

        frequency = {}
        for elem, freq in stack:
            frequency[elem] = frequency.get(elem, 0) + freq
        elements = sorted(frequency.keys())
        result = []
        for element in elements:
            result.append(element)
            if frequency[element] > 1:
                result.append(str(frequency[element]))
        return "".join(result)


    def getNumber(self, formula, start):
        j, n = start, len(formula)
        while j < n and formula[j].isdigit():
            j += 1
        if j == start:
            return 1, j
        return int(formula[start:j]), j
        
