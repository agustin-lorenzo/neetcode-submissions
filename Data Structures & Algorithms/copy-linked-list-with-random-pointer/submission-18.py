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
        old2copy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            old2copy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            old2copy[curr].next = old2copy[curr.next]
            old2copy[curr].random = old2copy[curr.random]
            curr = curr.next
        
        return old2copy[head]
