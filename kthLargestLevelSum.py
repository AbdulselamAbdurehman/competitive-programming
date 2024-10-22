# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = []
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()
            if len(level_sum) <= depth:
                level_sum.append(0)
            level_sum[depth] += node.val
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        if k > len(level_sum):
            return -1
        return sorted(level_sum, reverse=True)[k-1]
