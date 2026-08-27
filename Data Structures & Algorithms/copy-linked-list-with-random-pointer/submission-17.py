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
        o2c = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            o2c[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            o2c[curr].next = o2c[curr.next]
            o2c[curr].random = o2c[curr.random]
            curr = curr.next
        
        return o2c[head]