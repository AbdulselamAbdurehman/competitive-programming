class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort(reverse=True)
        i, j = 0, len(people)-1
        while i <= j:
            count += 1
            carry = people[i]
            if carry + people[j] <= limit:
                carry += people[j]
                j -= 1
            i += 1
        return count
