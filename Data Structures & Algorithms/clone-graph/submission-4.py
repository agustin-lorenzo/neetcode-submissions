"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2New = {}

        def dfs(n):
            if not n:
                return None
            
            if n not in old2New:
                old2New[n] = Node(n.val)
                for neigh in n.neighbors:
                    old2New[n].neighbors.append(dfs(neigh))
                    
            return old2New[n]
        
        return dfs(node)