# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        in_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        root_idx = 0
        def helper(left, right):
            nonlocal root_idx
            if left > right:
                return None
            node = TreeNode(preorder[root_idx])
            center = in_map[preorder[root_idx]]
            root_idx += 1 
            node.left = helper(left, center - 1)
            node.right = helper(center + 1, right)
            return node
        
        root = helper(0, n - 1)
        return root