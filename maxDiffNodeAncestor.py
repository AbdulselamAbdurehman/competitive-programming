# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0 #since it is absolute val
        stack = [[root, inf, -inf]] #[node, lowest, highest]
        while stack:
            curr, low, high = stack.pop()
            low, high = min(curr.val, low), max(curr.val, high)
            result = max(result, high - low)
            if curr.right:
                stack.append([curr.right, low, high])
            if curr.left:
                stack.append([curr.left, low, high])
        return result
