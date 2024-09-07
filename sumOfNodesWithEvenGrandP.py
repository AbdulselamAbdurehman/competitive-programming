# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(node):
            total = 0
            even = node.val % 2 == 0

            if node.right:
                total += dfs(node.right)
                if even and node.right.right:
                    total += node.right.right.val
                if even and node.right.left:
                    total += node.right.left.val
            if node.left:
                total += dfs(node.left)
                if even and node.left.right:
                    total += node.left.right.val
                if even and node.left.left:
                    total += node.left.left.val
            return total

        return dfs(root)
