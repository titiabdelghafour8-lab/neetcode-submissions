# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr, prev, tail, o_head = head, None, head, head
        checker = None
        count = 0
        while curr:
            check_count = 0
            checker = curr
            #check if there are actually more than k elements left
            while checker != None and check_count < k: 
                checker = checker.next
                check_count += 1
            if checker == None and check_count < k:
                if count >= 1:
                    tail.next = curr
                break
            if count >= 1:
                tmp = curr
            prev = None
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            count += 1
            if count == 1:
                o_head = prev
            if count >= 2:
                tail.next = prev
                tail = tmp
                
        return o_head









