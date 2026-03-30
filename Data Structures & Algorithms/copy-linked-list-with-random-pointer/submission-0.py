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
        # copy all nodes with next pointers first
        originalToCopy = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            originalToCopy[current] = copy
            current = current.next

        # second pass to copy random pointers
        current = head
        while current:
            copy = originalToCopy[current]
            copy.next = originalToCopy[current.next]
            copy.random = originalToCopy[current.random]
            current = current.next
        
        return originalToCopy[head]