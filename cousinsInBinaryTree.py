# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodeInfo = {} #{node.val: [depth, parent]}
        dq = deque([[root, 0, None]]) #[node, depth, parent]
        while dq:
            node, depth, parent = dq.pop()
            if node.val == x or node.val == y:
                nodeInfo[node.val] = [depth, parent]
            if node.left:
                dq.appendleft([node.left, depth + 1, node])
            if node.right:
                dq.appendleft([node.right, depth + 1, node])
        result = list(nodeInfo.values())
        return result[0][0] == result[1][0] and result[0][1] != result[1][1]
