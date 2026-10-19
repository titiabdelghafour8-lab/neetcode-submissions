# Definition for singly-linked list.
# class ListNode: 
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        if not head.next:
            return None
        length = 0
        curr = head
        while curr:
            length += 1 
            curr = curr.next
        
        count = 0
        prev = ListNode(0, head)
        curr = head
        while count < length - n:
            prev = curr
            curr = curr.next
            count += 1
        if length == n:
            return head.next
        prev.next = prev.next.next if prev.next else None
        return head 


        