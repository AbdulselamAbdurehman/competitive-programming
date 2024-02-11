# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append((p or None, q or None))
        while dq:
            tree1, tree2 = dq.pop()
            if tree1 and not tree2:
                return False
            if tree2 and not tree1:
                return False
            if not (tree1 or tree2):
                continue
            if tree1.val != tree2.val:
                return False
            dq.appendleft((tree1.left, tree2.left))
            dq.appendleft((tree1.right, tree2.right))
        return True
