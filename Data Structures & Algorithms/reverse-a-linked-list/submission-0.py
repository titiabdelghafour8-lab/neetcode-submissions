# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or head.next == None:
            return head
        prev_ptr = None
        current_ptr = head
        next_ptr = head.next
        while next_ptr != None:
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = next_ptr
            next_ptr = next_ptr.next
        current_ptr.next = prev_ptr
        
        return current_ptr