# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if length == n:
            return head.next

        slow, fast = head, head.next
        for i in range(n):
            fast = fast.next
        
        while fast:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        return head