# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        info = {} # {childValue:[childNode, parentNode]}
        dq = deque([root])
        while dq:
            node = dq.pop()
            if node.left:
                dq.append(node.left)
                info[node.left.val] = [node.left, node] 
            if node.right:
                dq.append(node.right)
                info[node.right.val] = [node.right, node]
        
        to_delete = set(to_delete)
        heads = []
        if root.val not in to_delete:
            heads.append(root)
        for node in info:
            child, parent = info[node][0], info[node][1]
            if node not in to_delete and parent.val in to_delete:
                heads.append(child)
            elif child.val in to_delete:
                leftChild, rightChild = parent.left, parent.right
                if leftChild and leftChild.val == child.val:
                    parent.left = None
                if rightChild and rightChild.val == child.val:
                    parent.right = None
        return heads
