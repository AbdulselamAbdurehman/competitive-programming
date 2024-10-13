"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
"""Time: O(n) Space: O(n)"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        levels = []
        dq = deque([[root, 0]]) # queue of [node, levelOfNode]

        while dq:
            node, level = dq.popleft()
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            for child in node.children:
                dq.append([child, level + 1])
        
        return levels            
