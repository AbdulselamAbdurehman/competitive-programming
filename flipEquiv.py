# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not (root1 or root2):
            return True
        if not (root1 and root2):
            return False
        
        if root1.val != root2.val:
            return False
        direct_equiv = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip_equiv = self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)
        
        return direct_equiv or flip_equiv
