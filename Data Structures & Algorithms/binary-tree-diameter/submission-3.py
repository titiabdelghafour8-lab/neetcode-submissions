# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 0
            return 1 + max(height(root.right), height(root.left)) 
        max_dm = 0
        if not root:
            return max_dm
        stack = [root]
        while stack:
            el = stack.pop()
            if not el:
                continue
            if not el.left and not el.right:
                continue
            if not el.left or not el.right:
                max_dm = max(1 + height(el.left) + height(el.right), max_dm)
            else:
                max_dm = max(2 + height(el.left) + height(el.right), max_dm)
            if el.right:
                stack.append(el.right)
            if el.left:
                stack.append(el.left)
        return max_dm
            
            
       
        
        


    