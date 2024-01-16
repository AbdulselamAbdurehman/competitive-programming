class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff, seen = [], set()
        condition = False
        for i in range(len(s)):
            if s[i] == goal[i]:
                if s[i] in seen:
                    condition = True
                else:
                    seen.add(s[i])
            else:
                diff += [i]
        if len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True
        if condition and len(diff) == 0:
            return True
        return False
