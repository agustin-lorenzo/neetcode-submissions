# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfway point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of list
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # alternate between two halves
        front, back = head, prev
        while back:
            temp1, temp2 = front.next, back.next
            front.next = back
            back.next = temp1
            front, back = temp1, temp2