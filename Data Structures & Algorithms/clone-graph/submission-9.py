"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old2new = {}

        def dfs(n):
            if n in old2new:
                return old2new[n]
            
            copy = Node(n.val)
            old2new[n] = copy
            for neigh in n.neighbors:
                copy.neighbors.append(dfs(neigh))

            return copy
        
        return dfs(node)