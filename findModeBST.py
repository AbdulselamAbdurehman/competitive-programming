# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter()
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            freq[curr.val] += 1
        result, maxFreq = [], 0
        for key in freq:
            if freq[key] < maxFreq:
                continue
            if freq[key] >  maxFreq:
                maxFreq, result = freq[key], []
            result.append(key)
        return result
