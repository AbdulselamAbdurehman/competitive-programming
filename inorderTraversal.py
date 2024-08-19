# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderHelper(root, result)
        return result

    def inorderHelper(self, node, order):
        if node:
            self.inorderHelper(node.left, order)
            order.append(node.val)
            self.inorderHelper(node.right, order)

