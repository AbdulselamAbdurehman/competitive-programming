# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_order = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()

            if len(level_order) <= level:
                level_order.append(0)
            
            level_order[level] += node.val
            
            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))
        queue = deque([(root, 0, root.val)]) # node, level, sibling_sum
        while queue:
            node, level, sibling_sum = queue.popleft()
            node.val += level_order[level] - sibling_sum - node.val

            if node.left and node.right:
                siblings = node.right.val + node.left.val
                queue.append((node.right, level + 1, siblings))
                queue.append((node.left, level + 1, siblings))
            elif node.left:
                queue.append((node.left, level + 1, node.left.val))
            elif node.right:
                queue.append((node.right, level + 1, node.right.val))

        return root
