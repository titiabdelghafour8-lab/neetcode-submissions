from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        n_edges = len(edges)
        visited = [False for i in range(n)]
        def bfs(i):
            nonlocal visited
            queue = deque([i])
            while queue:
                el = queue.popleft()
                for k in adj[el]:
                    if not visited[k]:
                        queue.append(k)
                        visited[k] = True
        bfs(0)
        for i in range(n):
            if not visited[i]:
                return False
        return (n_edges == n - 1)