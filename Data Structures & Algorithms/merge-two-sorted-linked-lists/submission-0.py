# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        end = dummy

        while list1 and list2:
            if list1.val < list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next = list2
                list2 = list2.next
            end = end.next
        
        if list1:
            end.next = list1
        elif list2:
            end.next = list2
        
        return dummy.next