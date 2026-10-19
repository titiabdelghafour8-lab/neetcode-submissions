class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zeros = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
        for el in zeros:
            for k in range(n):
                matrix[k][el[1]] = 0
            for l in range(m):
                matrix[el[0]][l] = 0
        
        