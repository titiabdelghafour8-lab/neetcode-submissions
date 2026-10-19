"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        pointers_map = {}
        curr = head 
        while curr:
            pointers_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                pointers_map[curr].next = pointers_map[curr.next]
            if curr.random:
                pointers_map[curr].random = pointers_map[curr.random]
            curr = curr.next
        
        return pointers_map[head]
        