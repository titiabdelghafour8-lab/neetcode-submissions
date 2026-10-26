from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        max_area = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    area = 1
                    queue = deque([(r, c)])
                    grid[r][c] = 0
                    while queue:
                        i, j = queue.popleft()
                        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < nr and 0 <= nj < nc and grid[ni][nj] == 1:
                                area += 1 
                                queue.append((ni, nj))
                                grid[ni][nj] = 0
                    max_area = max(area, max_area)
        return max_area



                       

                

        