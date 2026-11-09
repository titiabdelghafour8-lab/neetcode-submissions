class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}
        for el in prerequisites:
            adj[el[1]].append(el[0])
            
        # 0 visited, 1 visiting, 2 visited
        def dfs(curr, visited):
            visited[curr] = 1
            for i in adj[curr]:
                if visited[i] == 1:
                    return True
                if visited[i] == 0:
                    if dfs(i, visited):
                        return True
            visited[curr] = 2
            return False
        
        visited = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i, visited): 
                    return False
        return True


            

        