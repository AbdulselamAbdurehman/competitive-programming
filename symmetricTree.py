# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.areIdentical(root.left, root.right)
    
    def areIdentical(self, item1, item2):
        if item1 == item2 == None:
            return True
        if item1 == None or item2 == None or item1.val != item2.val:
            return False
        return self.areIdentical(item1.left, item2.right) and self.areIdentical(item1.right, item2.left)
