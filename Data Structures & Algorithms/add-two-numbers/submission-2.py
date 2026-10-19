# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits_sum = ListNode(0, None)
        final_sum = digits_sum
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            val1 = 0 if l1 == None else l1.val
            val2 = 0 if l2 == None else l2.val

            total = val1 + val2 + carry
            digits_sum.val = total % 10
            carry = total // 10

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            if l1 is not None or l2 is not None or carry != 0:
                digits_sum.next = ListNode(0, None)
                digits_sum = digits_sum.next
        return final_sum

            
            




        