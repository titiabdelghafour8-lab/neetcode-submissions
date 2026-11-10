class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return []
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        count = 0
        visited = [False for i in range(n)]
        def bfs(node):
            nonlocal visited, count
            if visited[node]:
                return
            queue = deque([node])
            visited[node] = True
            while queue:
                curr = queue.popleft()
                visited[curr] = True
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
            count += 1
        
        for i in range(n):
            bfs(i)

        return count
            