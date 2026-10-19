# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def getAncestorList(self, root, element) :
        L = [root]
        while (root.left or root.right):
            if root.val == element.val :
                break
            
            elif element.val > root.val :
                if root.right :
                    L.append(root.right)    
                    root = root.right
                else :
                    break
            else :
                if root.left :
                    L.append(root.left)
                    root = root.left
                else :
                    break
        return L
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        AP = self.getAncestorList(root, p)
        AQ = self.getAncestorList(root, q)
        N = min(len(AP), len(AQ))
        lca = None
        for i in range(0,N) :
            if AP[i] == AQ[i] :
                lca = AP[i]
            else :
                break
        AP.clear()
        AQ.clear()
        return lca