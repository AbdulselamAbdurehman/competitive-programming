# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, prev = None, None, TreeNode(float('-inf'))

        def traverse(node):
            nonlocal first, second, prev
            if not node:
                return

            traverse(node.left)

            if not first and prev.val >= node.val:
                first = prev
            if first and prev.val >= node.val:
                second = node

            prev = node
            traverse(node.right)

        traverse(root)
        first.val, second.val = second.val, first.val
