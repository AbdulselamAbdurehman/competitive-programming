class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        i, j = 1, n-2
        total_chem = skill[0]*skill[n-1]
        team1 = skill[0] + skill[n-1]
        while i < j:
            if skill[i] + skill[j] == team1:
                total_chem += skill[i]*skill[j]
                i += 1
                j -= 1
            else:
                return -1
        return total_chem
