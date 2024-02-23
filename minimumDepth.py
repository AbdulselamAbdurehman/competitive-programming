# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque()
        dq.append((root, 1))
        while dq:
            current = dq.pop()
            if current[0].left:
                dq.appendleft((current[0].left, current[1]+1))
            if current[0].right:
                dq.appendleft((current[0].right, current[1]+1))
            if not (current[0].left or current[0].right):
                return current[1]
