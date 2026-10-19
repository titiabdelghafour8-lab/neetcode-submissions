# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2
        return dummy.next    


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        
        
        first_half = self.mergeKLists(lists[:n//2])
        second_half = self.mergeKLists(lists[n//2:])
        return self.mergeTwoLists(first_half, second_half)











        