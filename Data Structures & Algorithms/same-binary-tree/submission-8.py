# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def eq(self, obj: Optional[TreeNode]) -> bool:
        if not obj:
            return False
        elif (not obj.left and self.left) or (not obj.right and self.right):
            return False
        elif (not self.left and obj.left) or (not self.right and obj.right):
            return False
        elif (not self.left and not obj.left) and (not self.right and not obj.right):
            return self.val == obj.val
        elif (not self.left and not obj.left) and (self.right and obj.right):
            return self.right.val == obj.right.val
        elif (not self.right and not obj.right) and (self.left and obj.left):
            return self.left.val == obj.left.val
        elif self.val != obj.val or self.left.val != obj.left.val or self.right.val != obj.right.val:
            return False
        return True
        

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        elif not p and q:
            return False
        if not (p.eq(q)):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        