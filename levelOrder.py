# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        dq = deque([(root, 1)])
        while dq:
            current = dq.pop()
            node, level = current[0], current[1]
            if level > len(result):
                result.append([])
            result[level-1].append(node.val)
            if node.left:
                dq.appendleft((node.left, level+1))
            if node.right:
                dq.appendleft((node.right, level+1))
        return result
