# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        stack = [root]
        while stack:
            current = stack.pop()
            if current.val > low and current.left:
                stack.append(current.left)
            if current.val < high and current.right:
                stack.append(current.right)
            if low <= current.val <= high:
                total += current.val
        return total
