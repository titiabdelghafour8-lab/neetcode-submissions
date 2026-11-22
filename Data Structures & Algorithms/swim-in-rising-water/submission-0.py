import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        heap = [(grid[0][0], (0, 0))]
        n, p = len(grid), len(grid[0])
        t_min = 0
        while True:
            water_level, cell = heapq.heappop(heap)
            if cell in visited:
                continue
            visited.add(cell)
            t_min = max(t_min, water_level)
            if cell == (n - 1, p - 1):
                return t_min
            for di, dj in directions:
                ni, nj = cell[0] + di, cell[1] + dj
                if ni >= n or ni < 0 or nj >= p or nj < 0:
                    continue
                heapq.heappush(heap, (grid[ni][nj], (ni, nj)))

        return -1