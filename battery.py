class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        dec = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - dec > 0:
                dec += 1
        return dec
