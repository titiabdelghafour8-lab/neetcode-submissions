from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2**31 - 1
        tresors = []
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        while queue:
                x, y, dist = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] == -1:
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    if grid[nx][ny] != INF:
                        continue
                    grid[nx][ny] = min(grid[nx][ny], dist + 1)
                    queue.append((nx, ny, dist + 1))
        
                




