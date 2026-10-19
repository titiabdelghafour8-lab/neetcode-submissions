# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_ptr = ListNode(0)
        list3 = dummy_ptr
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                dummy_ptr.next = list1
                list1 = list1.next
            else:
                dummy_ptr.next = list2
                list2 = list2.next
            dummy_ptr = dummy_ptr.next
        
        if list1 != None:
            dummy_ptr.next = list1
        elif list2 != None:
            dummy_ptr.next = list2

        
        return list3.next


    

        

        