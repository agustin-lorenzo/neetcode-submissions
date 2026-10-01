"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        o2c = {None: None}

        def dfs(n):
            if n in o2c:
                return o2c[n]
            
            clone = Node(n.val)
            o2c[n] = clone
            for neigh in n.neighbors:
                clone.neighbors.append(dfs(neigh))
            
            return clone
        
        dfs(node)
        return o2c[node]
