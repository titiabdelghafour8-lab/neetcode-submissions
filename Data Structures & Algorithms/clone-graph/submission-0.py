"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph_map = defaultdict(Node)
        node_copy = Node(node.val)
        def bfs(node):
            nonlocal graph_map, node_copy
            stack = deque([node])
            graph_map[node] = node_copy
            while stack:
                el = stack.pop()
                copy_el = graph_map[el]
                
                for neighbor in el.neighbors:
                    if neighbor not in graph_map:
                        neighbor_copy = Node(neighbor.val)
                        graph_map[neighbor] = neighbor_copy
                        stack.append(neighbor)
                    copy_el.neighbors.append(graph_map[neighbor])
        bfs(node)
        return node_copy








