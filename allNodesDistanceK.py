# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque([(target.val, 0)]) # Queue[(node, distance_from_target)]
        seen = set([target.val])
        graph = self.construct_graph(root)
        
        result = []
        while queue:
            curr, distance = queue.popleft()
            if distance > k:
                return result

            if distance == k:
                result.append(curr)
            
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    queue.append((neighbor, distance + 1))
                    seen.add(neighbor)
        return result




    def construct_graph(self, node):
        graph = defaultdict(list)
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)
        return graph
            
