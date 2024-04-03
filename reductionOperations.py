class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = Counter(nums) #hashmap of val: frequency
        arr = sorted(freq.keys())
        operations = 0
        for i in range(len(arr)):
            operations += i*freq[arr[i]]
        return operations
