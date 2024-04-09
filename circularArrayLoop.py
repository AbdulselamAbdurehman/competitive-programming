class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next_index(curr_index):
            return (curr_index + nums[curr_index]) % n
        
        for i in range(n):
            slow = fast = i
            while nums[slow] * nums[next_index(fast)] > 0 and \
                    nums[slow] * nums[next_index(next_index(fast))] > 0:
                slow = next_index(slow)
                fast = next_index(next_index(fast))
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
        return False
