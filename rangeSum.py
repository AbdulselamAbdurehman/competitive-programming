class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = self.get_prefix(nums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]

    def get_prefix(self, arr):
        cumulative = arr[0]
        for i in range(1, len(arr)):
            cumulative += arr[i]
            arr[i] = cumulative
        return arr



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
