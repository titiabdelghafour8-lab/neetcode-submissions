from collections import deque

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}
        def is_connected(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in adj[source]:
                if neighbor not in visited and is_connected(neighbor, target, visited):
                    return True
            return False
        
        for edge in edges:
            if is_connected(edge[0], edge[1], set()):
                return edge
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return res

        
    

