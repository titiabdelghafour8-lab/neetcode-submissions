# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -45679809345
        def maxim(root):
            nonlocal max_path
            if not root:
                return 0
            if not root.right and not root.left:
                max_path = max(max_path, root.val)
                return max(root.val, 0)
            left = maxim(root.left)
            right = maxim(root.right)
            max_path = max(max_path, root.val + left + right)
            return root.val + max(left, right)
        maxim(root)
        return max_path
            