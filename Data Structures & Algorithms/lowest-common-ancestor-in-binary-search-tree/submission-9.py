# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = TreeNode(val=p.val)
        p = TreeNode(min(q.val, p.val))
        q = TreeNode(max(temp.val, q.val))

        if p.val == root.val or q.val == root.val:
            return root
        elif q.val > root.val and p.val < root.val:
            return root
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        