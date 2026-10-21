class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = -float('inf')


        def search(node):
            nonlocal ans
            if node is None:
                return 0
            if node.val > ans:
                ans = node.val
            left = node.val + search(node.left)
            right = node.val + search(node.right)
            if  left + right - node.val > ans: 
                ans=left+right - node.val
            if left > ans:
                ans = left
            if right > ans:
                ans = right
            temp = max(left, right)
            return max(temp, node.val)
        search(root)
        return ans