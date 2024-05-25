# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode()
        stack1, stack2, stack = [root1], [root2], [root]
        while stack1 and stack2:
            node1, node2, node = stack1.pop(), stack2.pop(), stack.pop()
            node.val += node1.val
            node.val += node2.val
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
                node.right = TreeNode()
                stack.append(node.right)
            else:
                if node1.right:
                    node.right = node1.right
                elif node2.right:
                    node.right = node2.right
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
                node.left = TreeNode()
                stack.append(node.left)
            else:
                if node1.left:
                    node.left = node1.left
                elif node2.left:
                    node.left = node2.left
        return root
