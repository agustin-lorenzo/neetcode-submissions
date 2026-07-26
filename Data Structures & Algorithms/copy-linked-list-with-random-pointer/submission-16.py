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
        o2n = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            o2n[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            o2n[curr].next = o2n[curr.next]
            o2n[curr].random = o2n[curr.random]
            curr = curr.next
        
        return o2n[head]