class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[i-1])
    
        avgs = [-1]*len(nums)
        for i in range(len(avgs)):
            if i-k >= 0 and i+k < len(avgs):
                if i-k == 0:
                    avgs[i] = prefix[i+k]//(2*k + 1)
                else:
                    avgs[i] = (prefix[i+k] - prefix[i-k-1])//(2*k + 1)
        return avgs
