class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trusted_by, trusts = {}, set()
        for pair in trust:
            trusted_by[pair[1]] = trusted_by.get(pair[1], 0) + 1
            trusts.add(pair[0])
        print(trusted_by)
        print(trusts)
        for person in trusted_by:
            if trusted_by[person] == n-1 and not person in trusts:
                return person
        return -1
