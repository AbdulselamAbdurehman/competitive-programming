class TimeMap:

    def __init__(self):
        #Time: O(1), Space: O(1)
        self.timestamps = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        #Time: O(n), Space: O(n) for n calls
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #Time: O(logn), Space: O(1)
        stamps = self.timestamps[key]
        low, high = 0, len(stamps) - 1
        result = ""
        while low <= high:
            mid = low + (high - low)//2
            if stamps[mid][0] <= timestamp:
                result = stamps[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return result



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
