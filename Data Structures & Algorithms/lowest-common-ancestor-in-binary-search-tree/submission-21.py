# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tempq = q.val
        tempp = p.val
        p = TreeNode(min(tempp, tempq))
        q = TreeNode(max(tempq, tempp))
        ptr = root
        while ptr:
            if q.val >= ptr.val and p.val <= ptr.val:
                return ptr
            elif q.val > ptr.val and p.val > ptr.val:
                ptr = ptr.right
            elif q.val < ptr.val and p.val < ptr.val:
                ptr = ptr.left
        
        