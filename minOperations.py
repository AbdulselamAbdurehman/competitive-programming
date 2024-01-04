class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        operations = 0
        for num in frequency:
            if frequency[num] == 1:
                return -1
            if frequency[num] % 3 == 1:
                operations += frequency[num]//3 + 1
            else:
                operations += frequency[num]//3 + frequency[num]%3//2
        return operations
