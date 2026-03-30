# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        length = 0
        counter = head
        while counter:
            length += 1
            counter = counter.next
        
        # find nth node from the end
        idx = length - n
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        for i in range(idx):
            prev = current
            current = current.next

        prev.next = current.next
        return dummy.next
