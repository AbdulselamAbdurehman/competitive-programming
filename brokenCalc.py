class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target > startValue:
            operations += 1
            if target % 2:
                target += 1
            else:
                target //= 2
        return operations + startValue - target
