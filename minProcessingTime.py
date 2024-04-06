class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        print(processorTime)
        tasks.sort(reverse=True) # the early bird gets the longest flies
        print(tasks)
        j = maximum = 0 # pointer for tasks arr
        for i in range(len(processorTime)):
            current = max(tasks[j:j+4]) + processorTime[i]
            maximum = max(current, maximum)
            j += 4
        return maximum
