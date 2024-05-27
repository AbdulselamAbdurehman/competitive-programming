# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -inf, inf)

    def isValid(self, node, lowerLimit, upperLimit):
        if not node:
            return True
        curr = lowerLimit < node.val < upperLimit
        onLeft = self.isValid(node.left, lowerLimit, min(upperLimit, node.val))
        onRight = self.isValid(node.right, max(lowerLimit, node.val), upperLimit)
        return curr and onLeft and onRight
