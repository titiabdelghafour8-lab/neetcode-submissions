class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        dummy_ptr = head
        counter = 0
        while dummy_ptr != None: 
            dummy_ptr = dummy_ptr.next
            counter += 1

        center = head
        i = 0
        mid = (counter - 1) // 2
        while i < mid:
            center = center.next
            i += 1
            
        second_half = center.next
        center.next = None  
        
        prev = None
        curr = second_half
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        first = head
        second = prev
        while second != None:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2



