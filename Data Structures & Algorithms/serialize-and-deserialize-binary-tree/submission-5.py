# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

                
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            el = queue.popleft()
            if el:
                res.append(str(el.val))
                queue.append(el.left)
                queue.append(el.right)
            else:
                res.append('#')

        return '/'.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data_list = data.split('/')
        root = TreeNode(int(data_list[0]))
        queue = deque([root])
        n = len(data_list)
        i = 1
        while i < n and queue:
            el = queue.popleft()
            if data_list[i] != '#':
                el.left = TreeNode(int(data_list[i]))  
                queue.append(el.left)
            i += 1
            if data_list[i] != '#':
                el.right = TreeNode(int(data_list[i]))  
                queue.append(el.right)
            i += 1
        return root
