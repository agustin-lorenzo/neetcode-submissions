# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if n == length:
            return head.next
        
        # find nth node's location
        prev = None
        curr = head
        for i in range(length - n):
            prev = curr
            curr = curr.next
        
        # skip over nth node and delete
        prev.next = curr.next
        del curr # optional
        return head