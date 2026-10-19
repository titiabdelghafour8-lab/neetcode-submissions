# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        L = []
        is_bst = True
        prev = None
        def in_order(root):
            nonlocal is_bst, prev

            if not root:
                return
            in_order(root.left)
            if prev is not None and prev.val >= root.val:
                is_bst = False
                return
            L.append(root.val)
            prev = root
            in_order(root.right)
        in_order(root)
        return is_bst



        

        