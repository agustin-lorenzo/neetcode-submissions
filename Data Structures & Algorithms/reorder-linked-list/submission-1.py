# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find halfway point by iterating over list in O(n)
        # 2. use halfway point to determine temporary start
        # 3. use temp start to reverse second half of linked list
        # 4. use pointer to alternate between lists and change next pointers between them
        
        # 1. 
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        # 2.
        mid = head
        for _ in range(length // 2):
            mid = mid.next
        
        # 3. 
        prev = None
        current = mid
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head2 = prev

        dummy = ListNode()
        current = dummy        
        secondHalf = False
        
        while head and head2:
            if secondHalf:
                current.next = head2
                print(head2.val)
                head2 = head2.next
                secondHalf = False

            else:
                current.next = head
                print(head.val)
                head = head.next
                secondHalf = True
            current = current.next