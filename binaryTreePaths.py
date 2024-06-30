# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = [root]
        def backtrack():
            if not (path[-1].left or path[-1].right):
                result.append("->".join([str(p.val) for p in path]))
                return
            options = [path[-1].left, path[-1].right]
            for option in options:
                if option:
                    path.append(option)
                    backtrack()
                    path.pop()

        backtrack()
        return result
