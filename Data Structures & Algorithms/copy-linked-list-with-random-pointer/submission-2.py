"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        original2Copy = {}

        # recursively add node
        def add(node):
            if not node or node in original2Copy:
                return
            nodeCopy = Node(node.val)
            original2Copy[node] = nodeCopy

            if node.next:
                if node.next not in original2Copy:
                    add(node.next)
                nodeCopy.next = original2Copy[node.next]

            if node.random:
                if node.random not in original2Copy:
                    add(node.random)
                nodeCopy.random = original2Copy[node.random]

        add(head)
        return original2Copy[head]
            

