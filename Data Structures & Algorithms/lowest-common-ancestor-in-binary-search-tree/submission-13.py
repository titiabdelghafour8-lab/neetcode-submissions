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

        if p.val == root.val or q.val == root.val:
            return root
        elif q.val > root.val and p.val < root.val:
            return root
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        