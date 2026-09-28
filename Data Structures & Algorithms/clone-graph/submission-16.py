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

        def dfs(v):
            if v in o2c:
                return o2c[v]
            
            c = Node(v.val)
            o2c[v] = c

            for n in v.neighbors:
                c.neighbors.append(dfs(n))
            
            return c
        
        dfs(node)
        return o2c[node]