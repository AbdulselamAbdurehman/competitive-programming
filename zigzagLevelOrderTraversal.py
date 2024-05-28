# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        bfs, dq = [], deque([[root, 0]])
        while dq:
            curr, level = dq.pop()
            if level < len(bfs):
                bfs[-1].append(curr.val)
            else:
                bfs.append([curr.val])
            if curr.left:
                dq.appendleft([curr.left, level + 1])
            if curr.right:
                dq.appendleft([curr.right, level + 1])
        for i, row in enumerate(bfs):
            if i%2 == 1:
                bfs[i] = bfs[i][::-1]
        return bfs
