class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 unvisited, 1 visiting, 2 visited
        adj = {i: [] for i in range(numCourses)}
        for el in prerequisites:
            adj[el[0]].append(el[1])


        def dfs(curr, visited, path):
            visited[curr] = 1
            for i in adj[curr]:
                if visited[i] == 1:
                    return True
                if visited[i] == 0:
                    if dfs(i, visited, path):
                        return True
            visited[curr] = 2
            path.append(curr)
            return False
        
        visited = [0 for i in range(numCourses)]

        cycle = False
        path = []
        for i in range(numCourses):
            local_path = []
            if visited[i] == 0:
                if dfs(i, visited, local_path):
                    cycle = True
                    break
            path += local_path
        
        if not cycle:
            for i in range(numCourses):
                if i not in path:
                    path.append(i)
            return path
        return []

        
        

                
