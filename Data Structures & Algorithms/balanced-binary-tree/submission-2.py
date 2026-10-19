# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.height(root.right) - self.height(root.left)) > 1:
            return False
        if not root.right:
            return self.height(root) <= 1
        if not root.left:
            return self.height(root) <= 1
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

