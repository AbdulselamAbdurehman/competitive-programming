class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        recents = {}
        result = []
        for i in range(len(temperatures)-1, -1, -1):
            position = i
            for temp in recents:
                if temp > temperatures[i]:
                    if position == i:
                        position = recents[temp]
                    else:
                        position = min(position, recents[temp])
            recents[temperatures[i]] = i
            result.append(position-i)
        return reversed(result)
