# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        dq = deque([[root, root.val]]) # [current_node, path_sum upto this node]
        while dq:
            node, path_val = dq.pop()
            if node.left:
                dq.appendleft([node.left, path_val*10 + node.left.val])
            if node.right:
                dq.appendleft([node.right, path_val*10 + node.right.val])
            if not node.left and not node.right:
                total += path_val
        return total
