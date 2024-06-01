# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = [0]

        def helper(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            left_is_bst, left_sum, left_min, left_max = helper(node.left)
            right_is_bst, right_sum, right_min, right_max = helper(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = left_sum + node.val + right_sum
                min_val = min(left_min, node.val)
                max_val = max(right_max, node.val)
                max_sum[0] = max(max_sum[0], current_sum)
                return True, current_sum, min_val, max_val
            else:
                return False, 0, 0, 0
        
        helper(root)
        return max_sum[0]
