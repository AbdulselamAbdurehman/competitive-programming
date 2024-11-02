class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = self.getPrimes()
        leftMost, rightMost = len(nums), -1
        for i in range(len(nums)):
            if primes[nums[i]-1]:
                leftMost = min(i, leftMost)
                rightMost = max(i, leftMost)
        return rightMost - leftMost

    def getPrimes(self):
        UPPER = 101
        is_prime = [True]*UPPER
        is_prime[0] = False
        for i in range(2, UPPER):
            if not is_prime[i-1]:
                continue
            j = i
            while j + i < UPPER:
                j += i
                is_prime[j-1] = False

        return is_prime
