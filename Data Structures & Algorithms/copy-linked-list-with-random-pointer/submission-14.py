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
        original2copy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            original2copy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            original2copy[curr].next = original2copy[curr.next]
            original2copy[curr].random = original2copy[curr.random]
            curr = curr.next
        
        return original2copy[head]