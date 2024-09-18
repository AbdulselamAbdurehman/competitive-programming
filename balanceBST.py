# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.bst_to_arr(root)
        new_root = self.arr_to_bst(arr)
        return new_root


    def bst_to_arr(self, root):
        arr = []
        def inOrder(node):
            if node.left:
                inOrder(node.left)
            arr.append(node.val)
            if node.right:
                inOrder(node.right)

        inOrder(root)
        return arr

    def arr_to_bst(self, arr):
        if len(arr) == 1:
            return TreeNode(arr[0])
        elif len(arr) == 2:
            return TreeNode(arr[0], right=TreeNode(arr[1]))

        mid = len(arr)//2

        left_sub_tree = self.arr_to_bst(arr[:mid])
        right_sub_tree = self.arr_to_bst(arr[mid+1:])
        mid_node = TreeNode(arr[mid], left=left_sub_tree, right=right_sub_tree)
        return mid_node
