class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        p = len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        memo = {}
        def dp(i, j): #longest path from position (i, j)
            if i >= n or j >= p:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= p:
                    continue
                if matrix[ni][nj] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + dp(ni, nj))
            return memo[(i, j)]
        

        ans = 0
        for i in range(n):
            for j in range(p):
                ans = max(ans, dp(i, j))
        
        return ans
