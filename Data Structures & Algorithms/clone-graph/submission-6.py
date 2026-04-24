"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {None: None}

        def dfs(node):
            if not node:
                return None
            
            if node in old2new:
                return old2new[node]
            
            copy = Node(node.val)
            old2new[node] = copy # this HAS to go here before recursion!
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node)
