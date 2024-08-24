# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        N = len(nums)
        if N == 1:
            return TreeNode(val=nums[0])
        if N == 2:
            return TreeNode(val=nums[0], right=TreeNode(val=nums[1]))
        mid = TreeNode(nums[N//2])
        left = self.sortedArrayToBST(nums[:N//2])
        right = self.sortedArrayToBST(nums[N//2+1:])
        mid.left = left
        mid.right = right
        return mid
