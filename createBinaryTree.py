# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        def constructTree(val):
            node = TreeNode(val)
            leftVal, rightVal = nodes[val][0], nodes[val][1]

            if leftVal != None:
                if leftVal in nodes:
                    node.left = constructTree(leftVal)
                else:
                    node.left = TreeNode(leftVal)
            if rightVal != None:
                if rightVal in nodes:
                    node.right = constructTree(rightVal)
                else:
                    node.right = TreeNode(rightVal)
            return node

        nodes = {} #node: [left, right]
        children = set()
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = [None, None]
            if isLeft:
                nodes[parent][0] = child
            else:
                nodes[parent][1] = child
            children.add(child)
        for node in nodes:
            if node not in children:
                top = node # guaranteed to be executed
                break
        return constructTree(top)
