from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        NL = len(heights)
        NC = len(heights[0])
        def bfs(starting_cells):
            queue = deque(starting_cells)
            visited = set(starting_cells)
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= NL or nx < 0 or ny >= NC or ny < 0:
                        continue
                    if (nx, ny) in visited or heights[nx][ny] < heights[x][y]:
                        continue

                    visited.add((nx, ny))
                    queue.append((nx, ny))
            return visited
        starting_pacific = []
        for i in range(NL):
            starting_pacific.append((i, 0))
        for j in range(NC):
            starting_pacific.append((0, j))
        starting_atlantic = []
        for i in range(NL):
            starting_atlantic.append((i, NC - 1))
        for j in range(NC):
            starting_atlantic.append((NL - 1, j))

        visited_pacific = bfs(starting_pacific)
        visited_atlantic = bfs(starting_atlantic)

        return [[x, y] for (x, y) in list(visited_pacific & visited_atlantic)]

                        

