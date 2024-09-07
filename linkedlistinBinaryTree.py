# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node or tree_node.val != list_node.val:
                return False
            return dfs(list_node.next, tree_node.left) or dfs(list_node.next, tree_node.right)
        if dfs(head, root):
            return True
        if not root:
            return False
            
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
