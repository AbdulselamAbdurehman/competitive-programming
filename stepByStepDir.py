# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        dq = deque([(root, '')]) # (node, pathToNode)
        toStart = toDest = None
        while dq:
            node, path = dq.pop()
            if node.val == startValue:
                toStart = path
            if node.val == destValue:
                toDest = path
            if toStart != None and toDest != None:
                break

            if node.left:
                dq.append([node.left, path + 'L'])
            if node.right:
                dq.append([node.right, path + 'R'])

        i, m, n = 0, len(toStart), len(toDest)

        while i < m and i < n:
            if toStart[i] != toDest[i]:
                return 'U'*(m-i) + toDest[i:]
            i += 1
        return 'U'*(m-i) + toDest[i:]
        
