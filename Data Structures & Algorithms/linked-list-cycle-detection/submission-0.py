# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.visited = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return False  
        dummy_ptr = head 
        while dummy_ptr.next != None:
            dummy_ptr.visited = True
            if dummy_ptr.next.visited == True:
                return True
            dummy_ptr = dummy_ptr.next
        return False

