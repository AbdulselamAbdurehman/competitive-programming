# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        places = {} # holds {(row, col): []}
        dq = deque([[root, 0, 0]]) # holds the node, row and col indices repecitively
        while dq:
            node, row, col = dq.pop()
            if (row, col) not in places:
                places[(row, col)] = []
            places[(row, col)].append(node.val)
            if node.left:
                dq.appendleft([node.left, row + 1, col - 1])
            if node.right:
                dq.appendleft([node.right, row + 1, col + 1])
        locations = sorted(places.keys(), key=lambda location: location[1])
        result = {}
        for i, j in locations:
            if j not in result:
                result[j] = []
            # print(locations[(i, j)])
            result[j].extend(sorted(places[(i, j)]))
        return list(result.values())
