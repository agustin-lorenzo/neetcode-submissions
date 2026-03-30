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

        # Add all values where both l1 and l2 have a value for a power of 10
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            total = l1.val + l2.val + carry
            val = total % 10
            carry = total // 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        # Return beginning of list
        return dummy.next
