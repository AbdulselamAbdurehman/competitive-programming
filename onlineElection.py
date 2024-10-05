class TopVotedCandidate:
    # Time: O(n), Space: O(n)
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leading = [] # self.leading[i] = leader at times[i]    
        votes = defaultdict(int)
        for i in range(len(times)):
            votes[persons[i]] += 1
            if not self.leading or votes[self.leading[-1]] <= votes[persons[i]]:
                self.leading.append(persons[i])
            else:
                self.leading.append(self.leading[-1])

    def q(self, t: int) -> int:
        # Time: O(logn) Space: O(1)
        low, high = 0, len(self.times) - 1

        ans = len(self.times)
        while low <= high:
            mid = low + (high - low)//2
            if self.times[mid] == t:
                return self.leading[mid]
            elif self.times[mid] > t:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return self.leading[ans - 1]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
