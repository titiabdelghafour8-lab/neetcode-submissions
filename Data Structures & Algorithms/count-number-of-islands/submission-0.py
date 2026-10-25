from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        number = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    number += 1
                    queue = deque([(r, c)])
                    grid[r][c] = "0"
                    while queue:
                        i, j = queue.popleft()
                        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < nr and 0 <= nj < nc and grid[ni][nj] == "1":
                                queue.append((ni, nj))
                                grid[ni][nj] = "0"
        return number



                       

                

        