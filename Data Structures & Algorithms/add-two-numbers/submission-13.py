# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0

            s = l1v + l2v + carry
            place = s % 10
            carry = s // 10
            curr.next = ListNode(place)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return dummy.next