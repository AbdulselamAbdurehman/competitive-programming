# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves = []
        path = []
        def dfs(node):
            if not node.left and not node.right:
                leaves.append(path + [])
                return
            if node.left:
                path.append('L')
                dfs(node.left)
                path.pop()
            if node.right:
                path.append('R')
                dfs(node.right)
                path.pop()
        dfs(root)
        return self.countValidPairs(leaves, distance)

    def countValidPairs(self, leaves, distance):
        length, pairs = len(leaves), 0
        for i in range(length):            
            for j in range(i+1, length):
                leaf1, leaf2 = leaves[i], leaves[j]
                k, m, n = 0, len(leaf1), len(leaf2)
                while k < m and k < n:
                    if leaf1[k] != leaf2[k]:
                        break
                    k += 1
                if (m + n - 2*k) <= distance:
                    pairs += 1
            
        return pairs
