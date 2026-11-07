from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nl = len(grid)
        nc = len(grid[0])
        result = 0
        queue = deque()

        for i in range(nl):
            for j in range(nc):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            x, y, dist = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= nl or nx < 0 or ny >= nc or ny < 0:
                    continue
                if grid[nx][ny] != 1:
                    continue

                grid[nx][ny] = 2
                queue.append((nx, ny, dist + 1))
                result = max(result, dist + 1)
        

        for i in range(nl):
            for j in range(nc):
                if grid[i][j] == 1:
                    return -1 
        return result


